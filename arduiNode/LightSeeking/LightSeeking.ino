int mosfet1 = 6;
int mosfet2 = 8;
int leftSensor = 0;
int centerSensor = 1;

void setup() {
  pinMode(mosfet1, OUTPUT);
  pinMode(mosfet2, OUTPUT);
}

void loop() {
  int leftVal = analogRead(leftSensor);
  int centerVal = analogRead(centerSensor);
  
  
  if (leftVal > 650 && centerVal > 600) {
    digitalWrite(mosfet1, HIGH);
    digitalWrite(mosfet2, LOW);
  } else if (leftVal > 650) {
    digitalWrite(mosfet2, LOW);
    digitalWrite(mosfet1, HIGH);
  } else if (centerVal > 600) {
    digitalWrite(mosfet2, HIGH);
    digitalWrite(mosfet1, HIGH);
  } else if (leftVal < 650) {
    digitalWrite(mosfet2, HIGH);
    digitalWrite(mosfet1, LOW);
  } else {
    digitalWrite(mosfet1, LOW);
    digitalWrite(mosfet2, LOW);
  }
}




