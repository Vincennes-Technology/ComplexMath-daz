#!/usr/bin/python
#Diego A-Z

#From http://heinrichhartmann.com/blog/2014/12/14/Sensor-Monitoring-with-RaspberryPi-and-Circonus.html

# Analog Input with ADC0832 chip

#

# Datasheet: http://www.ti.com/lit/ds/symlink/adc0838-n.pdf

# Part of SunFounder LCD StarterKit

# http://www.sunfounder.com/index.php?c=show&id=21&model=LCD%20Starter%20Kit

# Wiring pins from Logan

#  Wiring pins
#ADC PINS
    # 1 of ADC - #17 on T-cobler

    # 2 of ADC - middle of potometer on T-cobler

    # 3 of ADC - ground on board

    # 4 of ADC - ground on board

    # 5 of ADC - #22 on T-cobler

    # 6 of ADC - #27 on T-cobler

    # 7 of ADC - #18 on T-cobler

    # 8 of ADC - to 3.3V on T-cobler

    # Hook up the two outside wires of the potometer

        # One of them to 3.3V on the cobblerand
        # The other wire to ground on the board



import time

import os

import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)



#  pins connected from the SPI port on the ADC to the Cobbler may be changed as pleased..

PIN_CLK = 18

PIN_DO  = 27

PIN_DI  = 22

PIN_CS  = 17



# setting up the SPI interface pins

GPIO.setup(PIN_DI,  GPIO.OUT)

GPIO.setup(PIN_DO,  GPIO.IN)

GPIO.setup(PIN_CLK, GPIO.OUT)

GPIO.setup(PIN_CS,  GPIO.OUT)



# readding SPI data from ADC8032

def getADC(channel):

	# 1. CS LOW.

        GPIO.output(PIN_CS, True)      # clear last transmission

        GPIO.output(PIN_CS, False)     # bring CS low



	# 2. Start clock

        GPIO.output(PIN_CLK, False)  # start clock low



	# 3. Input MUX address

        for i in [1,1,channel]: # start bit + mux assignment

                 if (i == 1):

                         GPIO.output(PIN_DI, True)

                 else:

                         GPIO.output(PIN_DI, False)



                 GPIO.output(PIN_CLK, True)

                 GPIO.output(PIN_CLK, False)



        # 4. read 8 ADC bits

        ad = 0

        for i in range(8):

                GPIO.output(PIN_CLK, True)

                GPIO.output(PIN_CLK, False)

                ad <<= 1 # shift bit

                if (GPIO.input(PIN_DO)):

                        ad |= 0x1 # set first bit



        # 5. reset

        GPIO.output(PIN_CS, True)



        return ad



if __name__ == "__main__":

        while True:

                print "ADC[0]: {}\t ADC[1]: {}".format(getADC(0), getADC(1))

                time.sleep(1)