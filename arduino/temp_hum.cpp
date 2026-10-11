#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float tempC = dht.readTemperature();
  float tempF = dht.readTemperature(true);

  if (isnan(humidity) || isnan(tempC)) {
    Serial.println("DHT Sensor Error");
    delay(1000);
    return;
  }

  Serial.print("Temp: ");
  Serial.print(tempC);
  Serial.print(" C | ");
  Serial.print(tempF);
  Serial.print(" F | Humidity: ");
  Serial.print(humidity);
  Serial.println("%");

  delay(1000);
}