#include <string.h>
#include "common/cc2530.h"
#include "common/utils.h"
#include "common/usart.h"
#include "common/clock.h"
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
        sendCharUart0(RxData);
      }
    }
}


