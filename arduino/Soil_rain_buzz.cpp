#define SOIL_PIN A0
#define RAIN_PIN 2
#define BUZZER_PIN 3

void setup() {
  Serial.begin(9600);

  pinMode(RAIN_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {

  int soilRaw = analogRead(SOIL_PIN);

  // 0% = dry, 100% = wet
  int soilPercent = map(soilRaw, 1023, 0, 0, 100);
  soilPercent = constrain(soilPercent, 0, 100);

  int rainValue = digitalRead(RAIN_PIN);

  bool rainDetected = (rainValue == LOW);

  Serial.print("Soil Moisture: ");
  Serial.print(soilPercent);
  Serial.println("%");

  if (rainDetected) {
    Serial.println("Rain Status: Rain Detected");
  }
  else {
    Serial.println("Rain Status: No Rain");
  }

  if (soilPercent < 40 && !rainDetected) {
    digitalWrite(BUZZER_PIN, HIGH);
    Serial.println("Irrigation Required");
  }
  else {
    digitalWrite(BUZZER_PIN, LOW);
    Serial.println("Irrigation Not Required");
  }

  Serial.println("--------------------");
  delay(1000);
}