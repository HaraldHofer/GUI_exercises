from Tkinter import *

window = Tk()

window.geometry('640x180')

def onButtonMinK():
    toCalc = input.get()
    answer = float(toCalc) * 1.60934
    output.config(text=answer)

def onButtonKinM():
    toCalc = input.get()
    answer = float(toCalc) * 0.621371
    output.config(text=answer)

greeting = Label(window, text='Der ultimative Umrechner von Kilometern in Meilen und umgekehrt!')
greeting.pack(side='top')

input = Entry(window)
input.pack()

ButtonMinK = Button(window, text='Meilen in Kilometer', command=onButtonKinM)
ButtonMinK.pack()

ButtonKinM = Button(window, text='Kilometer in Meilen', command=onButtonMinK)
ButtonKinM.pack()

Ergebnis = Label(window, text='Ergebnis: \n')
Ergebnis.pack()

output = Label(window, text='')
output.pack()

window.mainloop()