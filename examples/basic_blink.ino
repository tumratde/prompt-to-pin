// Blink with Serial Logging
// Blinks the onboard LED every 1 second and logs status via Serial

// Most Arduino boards have an onboard LED on pin 13
const int LED_PIN = LED_BUILTIN;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Set the LED pin as an output
  pinMode(LED_PIN, OUTPUT);
  
  // Initial log message
  Serial.println("Onboard LED Blink Sketch Started!");
}

void loop() {
  // Turn LED ON
  digitalWrite(LED_PIN, HIGH);
  Serial.println("LED is ON");
  delay(1000);  // Wait for 1 second
  
  // Turn LED OFF
  digitalWrite(LED_PIN, LOW);
  Serial.println("LED is OFF");
  delay(1000);  // Wait for 1 second
}