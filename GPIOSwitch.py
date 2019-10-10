#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  A class for controlling a single GPIO pin.
#  
#  License: MIT
#  
#  Copyright (c) 2019 Joerg Beckers

import RPi.GPIO as GPIO

class GPIOSwitch():
    """ This class encapsulates the switching on/off of a single output GPIO pin.
    """
    def __init__(self, gpioMode, pinNo, initialState, shouldWarn, highLevelActive):
        """ gpioMode: GPIO.BOARD or GPIO.BCM
            pinNo: number of the pin you want to control
            initialState: initial state of the pin when setting up control
            shouldWarn: set 'True' if the GPIO interface should warn if pin is already in use
            highLevelActive: 'True' means GPIO.HIGH equals active state
        """
        GPIO.setmode(gpioMode)
        GPIO.setwarnings(shouldWarn)
        
        self.pinNo = pinNo
        self.initialState = initialState
        self.highLevelActive = highLevelActive

        GPIO.setup(pinNo, GPIO.OUT, initial=initialState)

    def __del__(self):
        """ Destructor
        """
        self.cleanup()

    def cleanup(self):
        """ Cleanup GPIO interface.
        """
        GPIO.cleanup(self.pinNo)

    def switch(self, onoff):
        """ Switch the state of the pin depending on high or low level active.
        """
        if onoff == "on":
            on = GPIO.HIGH if self.highLevelActive else GPIO.LOW
            GPIO.output(self.pinNo, on)
        elif onoff == "off":
            off = GPIO.LOW if self.highLevelActive else GPIO.HIGH
            GPIO.output(self.pinNo, off)
        else:
            # Should raise an Exception here!?
            pass
        return self.isOn()

    def isOn(self):
        """ Read the current state of the pin. The return value depends on the activity state.
        """
        if GPIO.input(self.pinNo) == 1:
            ret = True if self.highLevelActive else False
            return ret
        if GPIO.input(self.pinNo) == 0:
            ret = False if self.highLevelActive else True
            return ret
