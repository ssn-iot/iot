from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(
    echo=24,
    trigger=23,
    max_distance=2.0
)

THRESHOLD_CM = 15.0

try:
    while True:
        distance_cm = sensor.distance * 100

        if distance_cm < THRESHOLD_CM:
            status = "SLOT OCCUPIED"
        else:
            status = "SLOT VACANT"

        print(
            f"Distance: {distance_cm:.1f} cm | "
            f"Status: {status}"
        )

        sleep(1)

except KeyboardInterrupt:
    print("Parking monitor stopped.")

finally:
    sensor.close()