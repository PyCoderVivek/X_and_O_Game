import turtle as t
from turtle import Screen
from tkinter import *
import O as os
import X as xs
screen=Screen()
def os11():
    os.O11()
def os12():
    os.O12()
def os13():
    os.O13()
def os21():
    os.O21()
def os22():
    os.O22()
def os23():
    os.O23()
def os31():
    os.O31()
def os32():
    os.O32()
def os33():
    os.O33()

# ----------------- #

canvas = screen.getcanvas()
button = Button(canvas.master, text="O_1,1", command=os11)
button.pack()
button.place(x=20, y=200)

canvas = screen.getcanvas()
button = Button(canvas.master, text="O_1,2", command=os12)
button.pack()
button.place(x=70, y=200)


canvas = screen.getcanvas()
button = Button(canvas.master, text="O_1,3", command=os13)
button.pack()
button.place(x=120, y=200)


canvas = screen.getcanvas()
button = Button(canvas.master, text="O_2,1", command=os21)
button.pack()
button.place(x=20, y=250)


canvas = screen.getcanvas()
button = Button(canvas.master, text="O_2,2", command=os22)
button.pack()
button.place(x=70, y=250)


canvas = screen.getcanvas()
button = Button(canvas.master, text="O_2,3", command=os23)
button.pack()
button.place(x=120, y=250)


canvas = screen.getcanvas()
button = Button(canvas.master, text="O_3,1", command=os31)
button.pack()
button.place(x=20, y=300)


canvas = screen.getcanvas()
button = Button(canvas.master, text="O_3,2", command=os32)
button.pack()
button.place(x=70, y=300)


canvas = screen.getcanvas()
button = Button(canvas.master, text="O_3,3", command=os33)
button.pack()
button.place(x=120, y=300)



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
t.mainloop()