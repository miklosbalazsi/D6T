#include <string.h>
#include "common/ioCC2530.h"
#include "common/utils.h"
#include "common/usart.h"
#include "common/clock.h"

char GET_CHIPID[] = {'F','E',0x01,0x01,0};
char GET_VERSION[] = {'F','E',0x0f,0x01,0};

char A = 'A';
char temp;
char Rxdata[50]; 
uchar RXTXflag = 1;// 1:reception status 3:transmission status
uchar datanumber = 0; 

void main(void)  {
  
  init32MhzClock();
  initUart0();
  enableReceivingUart0();

  P1DIR_2 = 1;
  P1DIR_3 = 1;
  P1_2 = 0;
  P1_3 = 0; 
  
       
  while(1){
    P1_2=0;
    P1_3=1;
    delayms(1000);  
      
    P1_2=1;
    P1_3 =0;
    delayms(1000); 
      
    if (RXTXflag == 3 && U0CSR_ACTIVE == 0 ){
      if ( my_strncmp(GET_CHIPID,Rxdata,datanumber) == 0 ) { sendCharUart0(CHIPID); }
      else if( my_strncmp(GET_VERSION,Rxdata,datanumber) == 0 ) { sendCharUart0(CHVER); }
      else {
        sendStringUart0(Rxdata, datanumber); //Send the recorded string.
      }
      enableReceivingUart0(); //reception is allowed
      RXTXflag = 1; //Recovery to the receiving state
      datanumber = 0; // pointer returns to 0
    }    
  } 
}

/****************************************************************
 The serial port receives a character: Once there is data from the serial port to CC2530, it will enter the interrupt,
 Assign the received data to the global variable temp.
****************************************************************/
#pragma vector = URX0_VECTOR
__interrupt void UARTRX0_ISR(void){
  temp = U0DBUF;
  if((temp!=0xff)&&(datanumber<50)){            // 0xff end char 
    Rxdata[datanumber++] = temp;
  }
  else{
    disableReceivingUart0();//reception prohibited
    RXTXflag = 3; //Enter the sending state
  }
}

#pragma vector = UTX0_VECTOR
__interrupt void UARTTX0_ISR(void){
}

