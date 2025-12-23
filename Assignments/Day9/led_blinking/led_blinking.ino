// ESP32 LED Blink using Arduino IDE

#define LED_PIN 2   // On-board LED is usually on GPIO 2 for ESP32 DevKit[web:10][web:16]

void setup() {
  pinMode(LED_PIN, OUTPUT);   // Set LED pin as output
}

void loop() {
  digitalWrite(LED_PIN, HIGH);  // LED ON
  delay(1000);                  // wait 1 second
  digitalWrite(LED_PIN, LOW);   // LED OFF
  delay(1000);                  // wait 1 second
}