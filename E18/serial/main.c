#include <string.h>
#include "lib/cc2530.h"
#include "main.h"

void main(void)  {
    P1DIR_2 = 1;
    P1DIR_3 = 1;
    P1_2 = 0;
    P1_3 = 0;
    
    init32MhzClock();
    initUart0();
    
    char RxData = 'A';
    while(1){
      
      P1_2=0;
      P1_3=1;
      delayms(2000);
            
      if( U0CSR_ACTIVE == 0 ){
      P1_2=1;
      P1_3 =0;
      delayms(2000);    
          U0DBUF = RxData;
          while (U0CSR_TX_BYTE != 1); //Wait for transmission ends 
          while ( UTX0IF != 1 ); // Wait for Send completed flag
          U0CSR_TX_BYTE = 0;
          UTX0IF = 0;
      }
    }
}

/*
 * Delay function
 */
void delayms(uint xms){
  uint i,j;
  for(i=xms;i>0;i--)
    for(j=587;j>0;j--);
}

/*
 * Initialise 32Mhz crystal system clock source
 */
void init32MhzClock(){
  
    /* Reset 0x04 
    * OSC32K_CALDIS
    *  Disable 32-kHz RC oscillator calibration.
    */
    setBit(SLEEPCMD,7);//0x84
    /* Reset 0xc9
    * Set the system clock source to 32MHZ crystal
    * clear CLKCONCMD.6 (OSC)
    */
    clearBit(CLKCONCMD,6);//0x89
    /* wait for the crystal to stabilize */
    while (CLKCONSTA != 0x89);
    /* Set the system main clock frequency to 32MHZ 
     * clear bit 2,1,0  01000111 10111000
     */
    CLKCONCMD &= ~0x47;//0x88
    /* wait for the crystal to stabilize */
    while (CLKCONSTA != 0x88);
}

/*
 * Initialize UART0 9600,8N1
 * Use Alt2 location P1.2, P1.3, P1.4, P1.5
 */
void initUart0(){
  
    /* Reset 0x00 
    * 0:Alt1 1:Alt2   CT-P1.2, RT-P1.3, Rx-P1.4, Tx-P1.5 
    */
    PERCFG |= bin(0,0,0,0,0,0,0,1);//0x01
    /* Reset 0x00 
    * P1 select 0: General Purpose 1: Peripheral purpose 
    *  P1.2, P1.3, P1.4, P1.5 should be Peripherial purpose
    */
    P1SEL  |= bin(0,0,1,1,0,0,0,0);//0x30
    /* Reset 0x00 
    * Set USART0 priority over USART1 and Timer1 
    * set P2SEL.6=1 (PRI3P1), P2SEL.3=1 (PRI0P1)
    */
    P2SEL  |= bin(0,1,0,0,1,0,0,0);//0x48
    
    /* Reset 0x00
    * Set UART method instead of SPI
    * Set U0CSR.7 = 1 (MODE)
    */
    setBit(U0CSR,7);//0x80
    
    /* Reset 0x00
     * U0GCR cooperates with U0BAUD
     * Baud rate is set to 115200
     */
    U0GCR |= 11;//0x0B
    U0BAUD |= 216;//0xD8
    
    /* Reset 0x02 
    *  Configure 8N1 
    */
    //U0UCR = 0x02;  Default
    
    /* Reset 0x00
    * IRCON0.1 (UTX0IF) interrupt flag is initially set to 1 (when sending and receiving)
    */
    UTX0IF = 0;
    
    //TODO    U0CSR |= 0X40;                             //receiving is allowed
 
    /* Reset 0x00
    *  Set IEN2.2=1 (UTX0IE)
    */
    setBit(IEN2,2);//0x04
    
        /* Reset 0x00
    *  Open the total interruption, receive the interruption
    *  Set IEN0.2=1 (URX0IE, IEN0.7=1 (EA)
    */
    IEN0 |= 0x84; //0x84
}