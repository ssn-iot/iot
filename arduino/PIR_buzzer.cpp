#define PIR_PIN 2
#define BUZZER_PIN 3

unsigned long lastAlertTime = 0;
unsigned long buzzerStartTime = 0;

bool buzzerActive = false;

void setup() {
  Serial.begin(9600);

  pinMode(PIR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  digitalWrite(BUZZER_PIN, LOW);
}

void loop() {

  unsigned long currentTime = millis();

  int motion = digitalRead(PIR_PIN);

  // Detect motion only if 10 seconds have passed
  if (motion == HIGH && !buzzerActive &&
      currentTime - lastAlertTime >= 10000) {

    lastAlertTime = currentTime;
    buzzerStartTime = currentTime;

    buzzerActive = true;
    digitalWrite(BUZZER_PIN, HIGH);

    Serial.print("Intrusion detected at ");
    Serial.print(currentTime / 1000.0);
    Serial.println(" seconds since startup.");
  }

  // Turn buzzer OFF after 3 seconds
  if (buzzerActive &&
      currentTime - buzzerStartTime >= 3000) {

    digitalWrite(BUZZER_PIN, LOW);
    buzzerActive = false;
  }
}