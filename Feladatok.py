#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok():

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


    def elsoFeladat(self):
        #menjen előre arobot 30 cm
        self.robot.straight(300)

    def masodikFeladat(self):
        #forduljon jobbra 90°-ot
        self.robot.drive(0,180)
        wait(500)
        self.robot.Stop(Stop.BRAKE)

    def harmadikFeladat(self):
        ut = 100
        fordul = 90
        # menjen előre
        self.robot.straight(ut)
        # menjen hátra
        self.robot.straight(ut*(-1))
        # foruljon 90°-ot jobbra
        self.robot.turn(fordul)
        # forduljon 90°-ot balra
        self.robot.turn(-1*fordul)

    def mozog1(self):
        self.jm.run(500)
        wait(1000)
        self.robot.stop(Stop.BRAKE)

    def mozog2(self):
        self.jm.run(500)
        self.bm.run(-200)
        wait(1000)
        self.robot.stop(Stop.BRAKE)

    def negyedikFeladat(self):
        self.robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
        self.robot.drive(100, 0)
        wait(1000)
        self.robot.stop()
        self.robot.drive(0, 90)
        wait(1000)
        self.robot.stop()
        self.robot.drive(-100, 0)
        wait(1000)
        self.robot.stop()
        self.robot.drive(0, -90)
        wait(1000)
        self.robot.stop()

    def koszon(self):
        # hang és színkezelés
        # fény beállítások narancssárga
        self.ev3.light.on(Color.RED)
        # beszélő beállításai, nyelv, nem, sebesség, mélység 
        self.ev3.speaker.set_speech_options('en','f2',100,400)
        # hangerő erősségének állítása
        self.ev3.speaker.set_volume(150)
        # robot beszéd
        # self.ev3.speaker.say("Hi, have a nice day!")
        print("Hi, have a nice day!")
        # fény kikapcsolása
        self.ev3.light.off()
        # fény beállítások piros
        self.ev3.light.on(Color.RED)
        # külső fájl lejátászása .wav
        #self.ev3.speaker.play_file("elephant_call.wav")
        #self.ev3.speaker.play_file("teve.wav")
        # beépített hangfájl lejátszása
        self.ev3.speaker.play_file(SoundFile.T_REX_ROAR)


    def csipog(self):
        pass
        #self.ev3.speaker.beep()
