const int buttonPin = 2;    // Button connected to digital pin 2
const int ledPin = 13;      // LED connected to digital pin 13

void setup() {
  // Initialize button pin as input with internal pull-up resistor
  pinMode(buttonPin, INPUT_PULLUP);
  
  // Initialize LED pin as output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Read the state of the button
  int buttonState = digitalRead(buttonPin);
  
  // If button is pressed (LOW due to pull-up resistor), turn on LED
  if (buttonState == LOW) {
    digitalWrite(ledPin, HIGH);  // Turn on LED
  } else {
    digitalWrite(ledPin, LOW);   // Turn off LED
  }
}