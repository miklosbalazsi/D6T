#define uint unsigned int
#define uchar unsigned char
#define bin(a,b,c,d,e,f,g,h) (a<<7)|(b<<6)|(c<<5)|(d<<4)|(e<<3)|(f<<2)|(g<<1)|(h<<0)
#define setBit(reg, bit) reg |= (1 << bit)
#define clearBit(reg, bit) reg &= ~(1 << bit)

void delayms(uint xms);
void initUart0();
void init32MhzClock();