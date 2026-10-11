import time
import RPi.GPIO as GPIO

PIR_PIN = 17
BUZZER_PIN = 22

ALERT_SECONDS = 3.0
COOLDOWN_SECONDS = 10.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.LOW)

start_time = time.monotonic()
last_alert_time = -COOLDOWN_SECONDS
buzzer_off_time = None
last_motion_state = GPIO.LOW

try:
    while True:
        now = time.monotonic()
        motion = GPIO.input(PIR_PIN)

        if buzzer_off_time is not None and now >= buzzer_off_time:
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            buzzer_off_time = None
            print("Buzzer: OFF")

        if motion == GPIO.HIGH and last_motion_state == GPIO.LOW:
            if now - last_alert_time >= COOLDOWN_SECONDS:
                elapsed = now - start_time

                print(
                    f"Intrusion detected at "
                    f"{elapsed:.1f} seconds since startup"
                )

                GPIO.output(BUZZER_PIN, GPIO.HIGH)
                print("Buzzer: ON")

                buzzer_off_time = now + ALERT_SECONDS
                last_alert_time = now
            else:
                print("Motion ignored: cooldown active.")

        last_motion_state = motion
        time.sleep(0.02)

except KeyboardInterrupt:
    print("System stopped.")

finally:
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    GPIO.cleanup()