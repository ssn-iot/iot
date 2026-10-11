import time
from datetime import datetime
from pathlib import Path

import RPi.GPIO as GPIO
from picamera2 import Picamera2

PIR_PIN = 17
COOLDOWN_SECONDS = 5.0

CAPTURE_DIR = Path("captures")
CAPTURE_DIR.mkdir(exist_ok=True)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

camera = Picamera2()

camera.configure(
    camera.create_still_configuration()
)

camera.start()
time.sleep(2)

last_capture_time = -COOLDOWN_SECONDS
previous_motion = GPIO.LOW

try:
    while True:
        now = time.monotonic()
        motion = GPIO.input(PIR_PIN)

        if motion == GPIO.HIGH and previous_motion == GPIO.LOW:
            if now - last_capture_time >= COOLDOWN_SECONDS:
                timestamp = datetime.now().strftime(
                    "%Y-%m-%d_%H-%M-%S"
                )

                filename = (
                    CAPTURE_DIR / f"image_{timestamp}.jpg"
                )

                camera.capture_file(str(filename))

                print(
                    f"Motion detected! Image saved: {filename}"
                )

                last_capture_time = time.monotonic()

            else:
                print(
                    "Motion detected, but cooldown is active."
                )

        previous_motion = motion
        time.sleep(0.02)

except KeyboardInterrupt:
    print("Camera monitoring stopped.")

finally:
    camera.stop()
    GPIO.cleanup()