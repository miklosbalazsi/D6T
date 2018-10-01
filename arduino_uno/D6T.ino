
#include <Wire.h>

#define D6T_ID 0x0A    // ID address for the D6T
#define D6T_CMD 0x4C   // Command to get information

// The D6T will return 35 bytes of data
int ReadBuffer[35];    // D6T Buffer
float ptat;            // reference temperatur
float ptat_16;
float tdata[16];       // temporary temperature data for 44L
float tpec;            // packet error check 



void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);
  Serial.println("Start...Wait 500");
  delay(500);
}

void loop() {
  
  // put your main code here, to run repeatedly:
  int i;
  int write_bytes;
  int endT;
  int bytes_recv;
  float tdata_16 = 0;
  float ptat_16 = 0;
  // Ask D6T for data
  Wire.beginTransmission(D6T_ID);
  write_bytes = Wire.write(D6T_CMD);
  endT = Wire.endTransmission();

  Serial.print("Write bytes num    : ");Serial.println(write_bytes);
  Serial.print("endTransmission RC : ");Serial.println(endT);  

  Wire.requestFrom(D6T_ID,35);
  bytes_recv =  Wire.available();
  Serial.print("Received bytes num : ");Serial.println(bytes_recv);
  //Getting data into buffer
  while(Wire.available())
  {
    ReadBuffer[i] = Wire.read();
    i++;
  }

  // Convert data into Celsius
  // Each temperature data has two parts, the Low and High significant bytes of the data. The full temperature data uses a 16 bit
  // signed that is 10 times the value of the celsius temperature. 
  // For example: the high byte data 0x00 and low byte data of 0xFA will translate to 0x00FA which is equivalent to 250. 
  // Dividing that by 10 will be 25.0 C or 77 F.
  ptat = (ReadBuffer[0]+256*ReadBuffer[1])*0.1; // reference Temp
  ptat_16 = ptat*16;
  Serial.print("ptat    : ");Serial.println(ptat);

  for( i=0; i<16; i++ )
  {
    
     tdata[i] = (ReadBuffer[(i*2+2)]+256*ReadBuffer[(i*2+3)])*0.1;
     tdata_16 = tdata_16+tdata[i];
    //Serial.print(i);
    //Serial.print(": ");
     if ( !(i % 4) ){ Serial.println();}
     Serial.print(tdata[i]);
     Serial.print("\t");
     
    //Serial.print(", ");
    //Serial.print("   ");
    //Serial.print(ReadBuffer[(i*2+2)]);
    // Serial.print(",");
    // Serial.println(ReadBuffer[(i*2+3)]);
   }
  Serial.println();
  Serial.print("ptat_16  : ");Serial.println(ptat_16);
  Serial.print("tdata_16 : ");Serial.println(tdata_16);  
  Serial.println();
  
  delay(5000);
  
}
