#include <WiFi.h>
#include <ArduinoMqttClient.h>
#include <DHT.h>

const char *ssid = "Tanisha";
const char *password = "tanisha21";

const char *host = "10.49.201.155";
unsigned int port = 1883;

#define DHT_PIN 4
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

WiFiClient wifiClient;
MqttClient publisher(wifiClient);

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // Connect to MQTT broker once
  if (!publisher.connect(host, port)) {
    Serial.println("MQTT connection failed");
    while (1);
  }
  Serial.println("Connected to MQTT Broker");
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  String data = "{\"temperature\":" + String(temperature) + ",\"humidity\":" + String(humidity) + "}";

  publisher.beginMessage("reading/dht");
  publisher.print(data);
  publisher.endMessage();

  Serial.println("Published:");
  Serial.println(data);

  delay(5000);
}

