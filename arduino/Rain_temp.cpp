#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

#define RAIN_PIN 3

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();

  pinMode(RAIN_PIN, INPUT);
}

void loop() {
  float temperature = dht.readTemperature();

  int rainValue = digitalRead(RAIN_PIN);

  if (isnan(temperature)) {
    Serial.println("DHT Sensor Error");
  }
  else {
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" C");

    if (rainValue == LOW) {
      Serial.println("Rain Status: 1 (Rain Detected)");
    }
    else {
      Serial.println("Rain Status: 0 (No Rain)");
    }
  }

  Serial.println("--------------------");
  delay(1000);
}