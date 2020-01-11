#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Switch on/off doorbell via command interface of raspend.
#  
#  Visit https://github.com/jobe3774/raspend to learn more about raspend.
# 
#  License: MIT
#  
#  Copyright (c) 2019 Joerg Beckers

import RPi.GPIO as GPIO
import time
import os
import logging
import argparse

from raspend import RaspendApplication
from GPIOSwitch import GPIOSwitch

def main():
    logging.basicConfig(filename='doorbell.log', level=logging.INFO)

    logging.info("Starting at {} (PID={})".format(time.asctime(), os.getpid()))

    # Check commandline arguments.
    cmdLineParser = argparse.ArgumentParser(prog="doorbell", usage="%(prog)s [options]")
    cmdLineParser.add_argument("--port", help="The port the server should listen on", type=int, required=True)
    cmdLineParser.add_argument("--gpio", help="The GPIO pin to use", type=int, required=True)

    try: 
        args = cmdLineParser.parse_args()
    except SystemExit:
        return

    try:
        # A relay is controlled via GPIO pin, which in turn controls the power supply of my bell transformer.
        doorBell = GPIOSwitch(GPIO.BOARD, args.gpio, GPIO.HIGH, False, False)

        myApp = RaspendApplication(args.port)

        # Use http://ip-of-your-raspberry:port/cmds to get a list of commands exposed by your raspberry.

        # 'doorBell.switch' can be called via http://ip-of-your-raspberry:port/cmd?name=doorBell.switch&onoff=off or via HTTP POST.
        myApp.addCommand(doorBell.switch)
        # 'doorBell.isOn' can be called via http://ip-of-your-raspberry:port/cmd?name=doorBell.isOn or via HTTP POST.
        myApp.addCommand(doorBell.isOn)

        myApp.run()

    except Exception as e:
        print ("An unexpected error occured. See 'doorbell.log' for more information.")
        logging.exception("Unexpected error occured!", exc_info = True)

    finally:
        # Release pin #12.
        doorBell.cleanup()

if __name__ == "__main__":
    main()
