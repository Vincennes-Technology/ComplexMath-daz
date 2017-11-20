#!/usr/bin/python
#Diego A-Z
#!/usr/bin/env python2.7
# script idea by Alex Eames http://RasPi.tv

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# Setting up GPIO 23 & 24 as the inputs. One up, the other down.
# 23 goes to GND when button pressed, and 24 will go to 3V3 (3.3V)
# this will help to display rising and falling edge detection
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# defining threaded callback function
# this will run in another thread when our event is detected
def my_callback(channel):
    print "Rising edge is detected in port 24 - regardless of expecting 23 to be pressed,"
    print "keep waiting for a falling edge - pres 23 anytime \n"

print "A button must be connected so once it is pressed  connected . Once it is pressed"
print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"
print "A second button is needed to be connected so that when pressed"
print "it will connect GPIO port 24 (pin 18) to 3V3 (pin 1)"
raw_input("ready? Press Enter \n>")

# The GPIO.add_event_detect() line below set things up so that
# when a rising edge is detected on port 24, regardless of whatever
# else is happening in the program, the function "my_callback" will be run
# It will happen even while the program is waiting for
# a falling edge on the other button.
GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback)

try:
    print "Waiting for falling edge on port 23"
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print "Falling edge detected!!!!!!!!!!!!!. End of the second lesson."

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit