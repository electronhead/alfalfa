"""
These classes perform simple GPIO operations on pins in addition to those actions
supplied in whendo.
"""
try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO

from whendo.core.action import Action
