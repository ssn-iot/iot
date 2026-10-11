import time
import Adafruit_DHT
import RPi.GPIO as GPIO

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
RAIN_PIN = 27

RAIN_ACTIVE_LOW = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(
    RAIN_PIN,
    GPIO.IN,
    pull_up_down=GPIO.PUD_UP
)

try:
    while True:
        humidity, temperature_c = Adafruit_DHT.read_retry(
            DHT_SENSOR, DHT_PIN
        )

        raw = GPIO.input(RAIN_PIN)

        raining = (
            raw == GPIO.LOW
            if RAIN_ACTIVE_LOW
            else raw == GPIO.HIGH
        )

        rain_status = 1 if raining else 0

        if temperature_c is None:
            print("Temperature: read failed")
        else:
            print(f"Temperature: {temperature_c:.1f}°C")

        print(f"Rain Status: {rain_status}")
        print("--------------------")

        time.sleep(1)

except KeyboardInterrupt:
    print("Monitoring stopped.")

finally:
    GPIO.cleanup()