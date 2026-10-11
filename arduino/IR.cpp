#define IR_PIN 2

int count = 0;

unsigned long lastDetectionTime = 0;

void setup() {
  Serial.begin(9600);

  pinMode(IR_PIN, INPUT);
}

void loop() {

  int sensorValue = digitalRead(IR_PIN);

  unsigned long currentTime = millis();

  // Most IR modules give LOW when object is detected
  if (sensorValue == LOW &&
      currentTime - lastDetectionTime >= 1000) {

    count++;

    lastDetectionTime = currentTime;

    Serial.print("Object detected! Total Count: ");
    Serial.println(count);
  }
}