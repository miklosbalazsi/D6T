#ifndef USART_H
#define USART_H

#include "compiler.h"
#include "cc2530.h"
#include "utils.h"

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

/*
*  Send one byte to USART0 Tx
*/
void sendCharUart0(char D){
  U0DBUF = D;
  while (U0CSR_TX_BYTE != 1); //Wait for transmission ends 
  while ( UTX0IF != 1 ); // Wait for Send completed flag
  U0CSR_TX_BYTE = 0;
  clearIrqFlag(IRCON2,1); // UTX0IF = 0; 
}

void enableReceivingUart0(){
    //TODO    U0CSR |= 0X40;                             //receiving is allowed
}

void disableReceivingUart0(){
   
}

#endif //USART_H