#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Palya():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 90)

    def palya2(self):
        self.robot.settings(straight_speed=800)
        self.robot.straight(2000)
        self.robot.turn(-135)
        self.robot.straight(1700)
        self.robot.turn(-133)
        self.robot.straight(2600)
        self.robot.turn(-135)
        self.robot.straight(1600)
        self.robot.turn(-135)
        self.robot.straight(1000)
        self.robot.turn(-720)
        self.robot.turn(720)
        self.robot.stop(Stop.BRAKE)

    def koszon(self):
        self.ev3.speaker.set_volume(100)
        self.ev3.speaker.play_file("teve.wav")

