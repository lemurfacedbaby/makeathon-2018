'''
Created on Jan 26, 2018

@author: Bryan
'''
import pyrebase
import time
#import RPi.GPIO as GPIO

def setupFirebase():
    config = {
    "apiKey": "AIzaSyDuZBIJtEyFK4hxyJtr-C9HO_R4Pix8kds",
    "authDomain": "",
    "databaseURL": "https://makeathon-2018.firebaseio.com/",
    "storageBucket": "",
    "serviceAccount": ""
    }

    firebase = pyrebase.initialize_app(config)  
    db = firebase.database()
    return db

'''
def gpioSetup():
    #Code for pin setup
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
'''    
    
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
if __name__ == '__main__':
    db = setupFirebase()
    #gpioSetup()
    while True:
        #Blue Beacon zone
        if int(db.child("bluebeacon").get().val()) == 0:
            #GPIO.output(3, GPIO.Low)
            #GPIO.output(5, GPIO.HIGH)
            print("Blue Light Off")
        else:
            #GPIO.output(3, GPIO.HIGH)
           # GPIO.output(5, GPIO.Low)
           print("BLue Light On")
        
        if int(db.child("greenbeacon").get().val()) == 0:
            #GPIO.output(8, GPIO8.Low)
            #GPIO.output(10, GPIO.HIGH)
            print("Green Light Off")
        
        else:
            #GPIO.output(8, GPIO.HIGH)
            #GPIO.output(10, GPIO.Low)
            print("Green Light On")
        
        if int(db.child("purplebeacon").get().val()) == 0:
            #GPIO.output(1, GPIO.Low)
            #GPIO.output(2, GPIO.HIGH)
            print("Purple Light Off")
        else:
            #GPIO.output(1, GPIO.HIGH)
            #GPIO.output(2, GPIO.Low)
            print("Purple Light On")
        time.sleep(1)
