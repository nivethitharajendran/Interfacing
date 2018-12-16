import RPi.GPIO as gpio
import time
#assigning the switches
s1 = 7
s2 = 11
s3 = 13
#setting up the input and output pins on board
gpio.setmode(gpio.BOARD)
gpio.setup(8,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(s1,gpio.IN)
gpio.setup(s2,gpio.IN)
gpio.setup(s3,gpio.IN)
n= input("Enter (Y/N):")
while n == "Y":
#if the switch1 is on
    if gpio.input(s1)==1:
        #led1 glows and the other two doesn't glow
        gpio.output(8,1)
        print("led on")
        gpio.output(12,0)
        gpio.output(16,0)
#if the switch2 is on
    elif gpio.input(s2)==1:
        #led2 glows and the other two doesn't glow
        gpio.output(12,1)
        print("led on")
        gpio.output(8,0)
        gpio.output(16,0)
#if the switch3 is on
    elif gpio.input(s3)==1:
        #led3 glows and the other two doesn't glow
        gpio.output(16,1)
        print("led on")
        gpio.output(8,0)
        gpio.output(12,0)
#if no switch is pressed
    else:
        #no bulb glows
        gpio.output(8,0)
        gpio.output(12,0)
        gpio.output(16,0)        
        print("led off")
import RPi.GPIO as gpio
import time
#assigning the switches
s1 = 7
s2 = 11
s3 = 13
#setting up the input and output pins on board
gpio.setmode(gpio.BOARD)
gpio.setup(8,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(s1,gpio.IN)
gpio.setup(s2,gpio.IN)
gpio.setup(s3,gpio.IN)
n= input("Enter (Y/N):")
while n == "Y":
#if the switch1 is on
    if gpio.input(s1)==1:
        #led1 glows and the other two doesn't glow
        gpio.output(8,1)
        print("led on")
        gpio.output(12,0)
        gpio.output(16,0)
#if the switch2 is on
    elif gpio.input(s2)==1:
        #led2 glows and the other two doesn't glow
        gpio.output(12,1)
        print("led on")
        gpio.output(8,0)
        gpio.output(16,0)
#if the switch3 is on
    elif gpio.input(s3)==1:
        #led3 glows and the other two doesn't glow
        gpio.output(16,1)
        print("led on")
        gpio.output(8,0)
        gpio.output(12,0)
#if no switch is pressed
    else:
        #no bulb glows
        gpio.output(8,0)
        gpio.output(12,0)
        gpio.output(16,0)        
        print("led off")
