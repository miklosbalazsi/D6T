#include <string.h>
#include "lib/cc2530.h"

#define uint unsigned int
#define uchar unsigned char
#define bin(a,b,c,d,e,f,g,h) (a<<7)|(b<<6)|(c<<5)|(d<<4)|(e<<3)|(f<<2)|(g<<1)|(h<<0)

/*
 * Delay function
 */
void delayms(uint xms){
  uint i,j;
  for(i=xms;i>0;i--)
    for(j=587;j>0;j--);
}

void initUart0(){
    CLKCONCMD &= ~0x40;         // Set the system clock source to 32MHZ crystal
    while (CLKCONSTA & 0x40);   // wait for the crystal to stabilize
    CLKCONCMD &= ~0x47;         // Set the system main clock frequency to 32MHZ

    PERCFG.0 = 1;           // 0:Alt1 1:Alt2   CT-P1.2, RT-P1.3, Rx-P1.4, Tx-P1.5
    P1SEL |= bin(0,0,1,1,1,1,0,0);        // P1 select 0: General Purpose 1: Peripheral purpose
    P2SEL &= bin(1,0,1,1,0,1,1,1);        // Set USART0 priority over USART1 and Timer1

    U0CSR |= 0x80; //UART method
    U0GCR |= 8;// U0GCR cooperates with U0BAUD
    U0BAUD |= 59; //Baud rate is set to 9600
    UTX0IF = 0;//UART0 TX interrupt flag is initially set to 1 (when sending and receiving)
//    U0CSR |= 0X40; //receiving is allowed
    IEN0 |= 0x84; //Open the total interruption, receive the interruption
    IEN2_UTX0IE = 1;
  /* 8N1 */
//  U0UCR = 0b00000010; // FLUSH, Flow, D9, Bit9, Parity, Spb, Stop, Start
}

void main(void)  {

    initUart0();

    char RxData = 'A';
    while(1){

      delayms(1000);
      if(UTX0IF == 0){
          U0DBUF = RxData;
          while (UTX0IF == 0); // Wait for Send completed flag
          UTX0IF = 0;
      }
  }
}