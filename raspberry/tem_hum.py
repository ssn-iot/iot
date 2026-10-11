import time
import Adafruit_DHT

SENSOR = Adafruit_DHT.DHT11
DATA_PIN = 4

try:
    while True:
        humidity, temperature_c = Adafruit_DHT.read_retry(
            SENSOR, DATA_PIN
        )

        if humidity is not None and temperature_c is not None:
            temperature_f = temperature_c * 9 / 5 + 32

            print(
                f"Temp: {temperature_c:.1f}°C | "
                f"{temperature_f:.1f}°F | "
                f"Humidity: {humidity:.0f}%"
            )
        else:
            print("Sensor read failed. Check wiring.")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")