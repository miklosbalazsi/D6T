#ifndef CLOCK_H
#define CLOCK_H

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

#endif //CLOCK_H