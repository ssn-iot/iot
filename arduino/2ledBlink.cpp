int led1 = 8;
int led2 = 9;

int blinkDelay = 500;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

  Serial.begin(9600);
  Serial.println("Type: fast, medium or slow");
}

void loop() {

  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();

    if (input == "fast") {
      blinkDelay = 200;
    }
    else if (input == "medium") {
      blinkDelay = 500;
    }
    else if (input == "slow") {
      blinkDelay = 1000;
    }
  }

  digitalWrite(led1, HIGH);
  digitalWrite(led2, LOW);
  delay(blinkDelay);

  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  delay(blinkDelay);
}