"""
These classes perform simple operations on pins.
"""

import RPi.GPIO as GPIO
import whendo.core.util as util
from whendo.core.action import Action

class SetPin(Action):
    """
    For the specified pin, sets to HIGH if on=True, to LOW if on=False.
    """
    pin:int
    on:bool

    def execute(self, tag:str=None, scheduler_info:dict=None):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.HIGH if self.on else GPIO.LOW)
            util.Output.pprint(lev_fil=util.Output.debug(), dictionary={'time':util.Now.s(), 'class':'SetPin', 'pin':self.pin, 'on':self.on, 'sched':scheduler_info})
        except Exception as exception:
            return exception

class TogglePin(Action):
    """
    For the specified pin, sets to HIGH if LOW, to LOW if HIGH.
    """
    pin:int

    def execute(self, tag:str=None, scheduler_info:dict=None):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, not GPIO.input(self.pin))
            util.Output.pprint(lev_fil=util.Output.debug(), dictionary={'time':util.Now.s(), 'class':'TogglePin', 'pin':self.pin, 'sched':scheduler_info})
        except Exception as exception:
            return exception

class Cleanup(Action):
    """
    Clean up the pins. See the docs for GPIO.cleanup().
    """

    def execute(self, tag:str=None, scheduler_info:dict=None):
        try:
            GPIO.cleanup()
        except Exception as exception:
            return exception