import datetime
import time
import cv2
from tkinter import *


class Timer(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()

    def MakeWidget(self):
        self.SetTime(self.nextTime)

    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)

    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        self.timestr = ('%02d' % minutes + ':' + '%02d' % seconds)

    def Start(self):
        if self.onRunning == 0:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1
            self.MakeWidget()

    def Stop(self):
        if self.onRunning == 1:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0
