
// ESP32 + MQ-2 gas sensor (analog read)

const int MQ2_PIN = 34;      // ADC pin connected to MQ-2 AO
const int GAS_THRESHOLD = 600;   // adjust after testing

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Not strictly required for analog input on ESP32, but OK to keep
  pinMode(MQ2_PIN, INPUT);

  Serial.println("MQ-2 Gas Sensor test");
}

void loop() {
  int gasValue = analogRead(MQ2_PIN);   // 0..4095 on most ESP32 boards
  Serial.print("MQ-2 Sensor Value: ");
  Serial.println(gasValue);

  if (gasValue > GAS_THRESHOLD) {
    Serial.println("Gas Detected!");
  } else {
    Serial.println("No Gas Detected.");
  }

  Serial.println("------------------------");
  delay(1000);   // 1 second between readings
}
