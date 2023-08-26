import turtle as t
from turtle import Screen
from tkinter import *
import O as os
import X as xs
screen=Screen()

def xs11():
    xs.x11()
def xs12():
    xs.x12()
def xs13():
    xs.x13()
def xs21():
    xs.x21()
def xs22():
    xs.x22()
def xs23():
    xs.x23()
def xs31():
    xs.x31()
def xs32():
    xs.x32()
def xs33():
    xs.x33()

# ---------------- #

canvas = screen.getcanvas()
button = Button(canvas.master, text="X_1,1", command=xs11)
button.pack()
button.place(x=570, y=200)

canvas = screen.getcanvas()
button = Button(canvas.master, text="X_1,2", command=xs12)
button.pack()
button.place(x=620, y=200)

canvas = screen.getcanvas()
button = Button(canvas.master, text="X_1,3", command=xs13)
button.pack()
button.place(x=670, y=200)

canvas = screen.getcanvas()
button = Button(canvas.master, text="X_2,1", command=xs21)
button.pack()
button.place(x=570, y=250)

canvas = screen.getcanvas()
button = Button(canvas.master, text="X_2,2", command=xs22)
button.pack()
button.place(x=620, y=250)

canvas = screen.getcanvas()
button = Button(canvas.master, text="X_2,3", command=xs23)
button.pack()
button.place(x=670, y=250)

canvas = screen.getcanvas()
button = Button(canvas.master, text="X_3,1", command=xs31)
button.pack()
button.place(x=570, y=300)

canvas = screen.getcanvas()
button = Button(canvas.master, text="X_3,2", command=xs32)
button.pack()
button.place(x=620, y=300)

canvas = screen.getcanvas()
button = Button(canvas.master, text="X_3,3", command=xs33)
button.pack()
button.place(x=670, y=300)