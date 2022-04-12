#!/usr/bin/ python3
#! /usr/bin/env python

import smbus, time, threading
import RPi.GPIO as GPIO

bus = smbus.SMBus(1)

def mario_sound(frq):
    try:
        bus.write_block_data(0x44, 0, [8, frq])
    except:
        pass

def trois_colors(frq):
    try:
        bus.write_byte(0x44, 11)
        time.sleep(frq/1000)
        bus.write_byte(0x44, 12)
        time.sleep(frq/1000)
        bus.write_byte(0x44, 13)
        time.sleep(frq/1000)
    except:
        pass

def blinkingRGB(arg):
    t = threading.currentThread()
    try:
        while getattr(t, "do_run", True):
            bus.write_byte(0x44, 11)
            time.sleep(0.15)
            bus.write_byte(0x44, 12)
            time.sleep(0.2)
            bus.write_byte(0x44, 13)
            time.sleep(0.25)
    except:
        pass

def trois_colors_250():
    try:
        for i in range(50):
            bus.write_byte(0x44, 11)
            time.sleep(0.25)
            bus.write_byte(0x44, 12)
            time.sleep(0.25)
            bus.write_byte(0x44, 13)
            time.sleep(0.25)
    except:
        pass

def flash_green():
    try:
        t = threading.Thread(target=mario_s)
        t.start()
        for i in range(20):
            bus.write_byte(0x44, 12)
            time.sleep(0.1)
    except:
        pass

def mario_s():
    mario_sound(2640)
    time.sleep(0.15)
    mario_sound(2640)
    time.sleep(0.3)
    mario_sound(2640)
    time.sleep(0.3)
    mario_sound(2040)
    time.sleep(0.1)
    mario_sound(2640)
    time.sleep(0.3)
    mario_sound(3080)
    time.sleep(0.55)
    mario_sound(1520)
    time.sleep(0.575)

def led_1_ctrl(state): ### state should be 0 or 1
    try:
        bus.write_block_data(0x44, 0, [10, state])
    except:
        pass

def led_2_ctrl(state):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4,GPIO.OUT)
    if state == 1:
        GPIO.output(4, GPIO.HIGH)
    elif state == 0:
        GPIO.output(4, GPIO.LOW)
