#ifndef UTILS_H
#define UTILS_H

#define uint unsigned int
#define uchar unsigned char
#define bin(a,b,c,d,e,f,g,h) (a<<7)|(b<<6)|(c<<5)|(d<<4)|(e<<3)|(f<<2)|(g<<1)|(h<<0)
#define setBit(reg, bit) reg |= (1 << bit)
#define clearBit(reg, bit) reg &= ~(1 << bit)
#define clearIrqFlag(irq, bit) irq = ~(1 << bit)

/*
 * Delay function
 */
void delayms(uint xms){
  uint i,j;
  for(i=xms;i>0;i--)
    for(j=587;j>0;j--);
}


uint my_strncmp(char* str,char* rxData, uint len){
  uint str_num = strlen(str);
  if ( str_num != len ) {return 1;}
  for(uint i = 0; i<str_num; i++){
    if (str[i] != rxData[i]) {return 1;}
  }
  return 0;
}

#endif //UTILS_H