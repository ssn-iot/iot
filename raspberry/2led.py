import RPi.GPIO as GPIO
import time
import threading

LED1 = 17
LED2 = 27

delays = {
    "fast": 0.2,
    "medium": 0.5,
    "slow": 1.0
}

blink_delay = 0.5
lock = threading.Lock()
running = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)

def read_commands():
    global blink_delay, running

    while running:
        try:
            command = input(
                "Speed (fast/medium/slow/quit): "
            ).strip().lower()
        except EOFError:
            running = False
            break

        if command in delays:
            with lock:
                blink_delay = delays[command]
            print("Speed changed to", command)

        elif command in ("quit", "exit"):
            running = False

        else:
            print("Enter fast, medium, slow, or quit.")

threading.Thread(
    target=read_commands,
    daemon=True
).start()

try:
    while running:
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.LOW)

        with lock:
            delay = blink_delay
        time.sleep(delay)

        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)

        with lock:
            delay = blink_delay
        time.sleep(delay)

except KeyboardInterrupt:
    pass

finally:
    running = False
    GPIO.output(LED1, GPIO.LOW)
    GPIO.output(LED2, GPIO.LOW)
    GPIO.cleanup()