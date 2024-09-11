#include <OneWire.h>
#include <DallasTemperature.h>

// Pin definitions
#define ONE_WIRE_BUS 2    // DS18B20 temperature sensor pin
#define TDS_PIN A0        // TDS sensor analog pin
#define TURBIDITY_PIN A1  // Turbidity sensor analog pin
#define PH_PIN A2         // pH sensor analog pin

// Setup OneWire and DallasTemperature for the DS18B20 sensor
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// Variables to store sensor readings
float temperature, tds, turbidity, ph, turbidityNTU;

void setup() {
  Serial.begin(9600);  // Begin serial communication with ESP
  sensors.begin();     // Initialize the DS18B20 temperature sensor
}

void loop() {
  // Read temperature
  sensors.requestTemperatures();
  temperature = sensors.getTempCByIndex(0);

  // Read TDS
  tds = analogRead(TDS_PIN);
  tds = tds * (5.0 / 1024.0) * 1000;  // Example conversion, adjust as needed

  // Read turbidity
  turbidity = analogRead(TURBIDITY_PIN);

  // Convert turbidity to NTU
  // Example conversion formula for turbidity to NTU
  // NTU = -1120.4 * voltage^2 + 5742.3 * voltage - 4352.9 (for a typical sensor)
  float voltage = turbidity * (5.0 / 1024.0);  // Convert analog value to voltage
  turbidityNTU = -1120.4 * voltage * voltage + 5742.3 * voltage - 4352.9;

  // Read pH
  ph = analogRead(PH_PIN);
  ph = 3.5 * ph * (5.0 / 1024.0);  // Example conversion, adjust as needed

  // Send JSON-style readings over Serial to ESP
  Serial.print("{\"temperature\":");
  Serial.print(temperature);
  Serial.print(",\"tds\":");
  Serial.print(tds);
  Serial.print(",\"turbidity\":");
  Serial.print(turbidityNTU);
  Serial.print(",\"ph\":");
  Serial.print(ph);
  Serial.println("}");

  delay(5000);  // Wait for 5 seconds before next reading
}
