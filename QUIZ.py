# -*- coding: utf-8 -*-

from Tkinter import *
import random

window = Tk()
window.geometry()


greeting = Label(text='QUIZ\nWähle eine eine der vier angegebenen Antworten.')
greeting.pack(side=TOP)

Frage = Label(text='Fragetext Fragetext Fragetext Fragetext Fragetext Fragetext Fragetext Fragetext?\n')
Frage.pack()

BtnA = Button(text='A: ')
BtnA.pack()
antA = Label(text='Antwortmöglichkeit A')
antA.pack()

BtnB = Button(text='B: ')
BtnB.pack()
antB = Label(text='Antwortmöglichkeit B')
antB.pack()

BtnC = Button(text='C: ')
BtnC.pack()
antC = Label(text='Antwortmöglichkeit C')
antC.pack()

BtnD = Button(text='D: ')
BtnD.pack()
antD = Label(text='Antwortmöglichkeit D')
antD.pack()

window.mainloop()