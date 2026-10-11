import time
import RPi.GPIO as GPIO

IR_PIN = 17
DEBOUNCE_SECONDS = 1.0

count = 0
last_detection = -DEBOUNCE_SECONDS

GPIO.setmode(GPIO.BCM)
GPIO.setup(
    IR_PIN,
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP
)

try:
    while True:
        now = time.monotonic()
        sensor_state = GPIO.input(IR_PIN)

        if sensor_state == GPIO.LOW:
            if now - last_detection >= DEBOUNCE_SECONDS:
                count += 1

                print(
                    f"Object detected! Total Count: {count}"
                )

                last_detection = now

        time.sleep(0.02)

except KeyboardInterrupt:
    print("Counting stopped.")

finally:
    GPIO.cleanup()