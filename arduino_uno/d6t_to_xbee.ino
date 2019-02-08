#include <Wire.h>
#define D6T_ID 0x0A    // ID address for the D6T
#define D6T_CMD 0x4C   // Command to get information

// The D6T will return 35 bytes of data
int ReadBuffer[35];    // D6T Buffer
float ptat;            // reference temperature
float ptat_16;
float tdata[16];       // temporary temperature data for 44L
float tpec;            // packet error check 
byte checksum = 0x00;

byte message[53] = {0x7E, 0x00, 0x31, 0x10, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFE, 0x00, 0x00, 
                    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 
                    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 
                    0x5B};

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);
  delay(500);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sum =  0x20E;
  int i = 17;
  int write_bytes;
  int endT;

  Wire.beginTransmission(D6T_ID);
  write_bytes = Wire.write(D6T_CMD);
  endT = Wire.endTransmission();

  Wire.requestFrom(D6T_ID,35);
  while(Wire.available())
  {
    
    message[i] = Wire.read();
    sum = sum + message[i];
    i++;
  }
 
  checksum = 0xFF - (sum & 0xFF);
  message[52] = checksum;

 Serial.write(message , 53 );
 delay(5000);
}
