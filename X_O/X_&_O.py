import turtle as t
from turtle import Screen
from tkinter import *
import O as os
import X as xs
import drawO
import drawX
# -------------------------- #
t.title("X and O")
screen = Screen()
screen.setup(width=800, height=800)
t.hideturtle()
t.bgcolor("black")
t.color("green")
t.penup()
t.goto(-300, 250)
t.write("PLAYER 1",font=("Arial",18,"bold"))
t.pendown()
t.penup()
t.goto(150, 250)
t.write("PLAYER 2",font=("Arial",18,"bold"))
t.penup()
t.goto(-110, 110)
t.pendown()
t.forward(250)
t.penup()
t.goto(-110, 50)
t.pendown()
t.forward(250)
t.penup()
t.goto(-28, 200)
t.right(90)
t.pendown()
t.forward(250)
t.penup()
t.goto(50, 200)
t.pendown()
t.forward(250)


t.done()
t.clear()
