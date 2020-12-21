//www.elegoo.com
//2016.06.13

#include <SimpleDHT.h>
#define DHT11_PIN A1
// for DHT11, 
//      VCC: 5V or 3V
//      GND: GND
//      DATA: 2
int pinDHT11 = 2;
SimpleDHT11 dht11;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // start working...
  
  // read with raw sample data.
  byte temperature = 0;
  byte humidity = 0;
  byte data[40] = {0};
  dht11.read(DHT11_PIN, &temperature, &humidity, data);
  Serial.print((int)temperature); Serial.print(","); Serial.println((int)humidity);
  
  // DHT11 sampling rate is 1HZ.
  delay(2000);
}
