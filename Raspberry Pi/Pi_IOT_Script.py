import RPi.GPIO as GPIO
 # inport the GPIO libraries for PI

GPIO.setup(3, GPIO.OUT) #Code for pin setup
GPIO.setup(5, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

#GPIO.output(channel, GPIO.HIGH) # set channel for being output of 3.3 V
# two options for output (.HIGH0 := 3.3V) & ( .LOW := .0 V)

# Right now we have four different stated for two buttons Binary on off

# Pin Designation:
# Pin 3 Outlet 1 on
# Pin 5 outlet 1 off
# Pin 8 outlet 2 on
# Pin 10 outlet 2 off

# Set objects from firebase: All states should be binary to designate signal or no signal to the optocoupler
# Outlet state 1 for on and outlet state 0 for off
outletstate1 = 1

outletstate2 = 0

if outletstate1 == 1:
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.Low)
else:
    GPIO.output(3, GPIO.Low)
    GPIO.output(5, GPIO.HIGH)

if outletstate2 == 1:
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(10, GPIO.Low)
else:
    GPIO.output(8, GPIO.Low)
    GPIO.output(10, GPIO.HIGH)
