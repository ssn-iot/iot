import time
import RPi.GPIO as GPIO

PIR_PIN = 17
RELAY_PIN = 27

LIGHT_SECONDS = 10.0

# Change to True if the relay is active LOW.
RELAY_ACTIVE_LOW = False

def set_relay(on):
    if RELAY_ACTIVE_LOW:
        GPIO.output(
            RELAY_PIN,
            GPIO.LOW if on else GPIO.HIGH
        )
    else:
        GPIO.output(
            RELAY_PIN,
            GPIO.HIGH if on else GPIO.LOW
        )

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(RELAY_PIN, GPIO.OUT)

set_relay(False)

relay_on = False
last_motion_time = None
last_printed_second = None

try:
    while True:
        now = time.monotonic()
        motion = GPIO.input(PIR_PIN)

        if motion == GPIO.HIGH:
            last_motion_time = now

            if not relay_on:
                relay_on = True
                set_relay(True)

                print("Motion detected!")
                print("Relay: ON")
                print("LED: ON")

        if relay_on and last_motion_time is not None:
            elapsed = now - last_motion_time

            if elapsed >= LIGHT_SECONDS:
                relay_on = False
                set_relay(False)

                print("No motion for 10 seconds.")
                print("Relay: OFF")
                print("LED: OFF")

                last_printed_second = None

            else:
                remaining = int(
                    LIGHT_SECONDS - elapsed + 0.999
                )

                if remaining != last_printed_second:
                    print(f"Timer remaining: {remaining} seconds")
                    last_printed_second = remaining

        time.sleep(0.02)

except KeyboardInterrupt:
    print("System stopped.")

finally:
    set_relay(False)
    GPIO.cleanup()