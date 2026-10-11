#define PIR_PIN 2
#define RELAY_PIN 3

unsigned long lastMotionTime = 0;

const unsigned long ON_TIME = 10000;

// Change to LOW if your relay module is active LOW
#define RELAY_ON HIGH
#define RELAY_OFF LOW

void setup() {
  Serial.begin(9600);

  pinMode(PIR_PIN, INPUT);
  pinMode(RELAY_PIN, OUTPUT);

  digitalWrite(RELAY_PIN, RELAY_OFF);

  Serial.println("System Ready");
}

void loop() {

  unsigned long currentTime = millis();

  int motion = digitalRead(PIR_PIN);

  if (motion == HIGH) {

    lastMotionTime = currentTime;

    digitalWrite(RELAY_PIN, RELAY_ON);

    Serial.println("Motion: DETECTED");
    Serial.println("Relay: ON");
  }

  if (currentTime - lastMotionTime >= ON_TIME) {

    digitalWrite(RELAY_PIN, RELAY_OFF);

    Serial.println("Motion: NOT DETECTED");
    Serial.println("Relay: OFF");
    Serial.println("Timer: 10 seconds completed");
  }

  delay(100);
}