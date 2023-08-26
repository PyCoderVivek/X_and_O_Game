import turtle

# Create a function to be called when the button is clicked
def button_click(x, y):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.write("Win", align="center", font=("Arial", 24, "bold"))

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Button Click Example")

# Create a turtle button
button = turtle.Turtle()
button.shape("square")
button.color("red")
button.penup()
button.goto(0, -50)
button.write("Click Me!", align="center", font=("Arial", 24, "bold"))

# Register the button click event
button.onclick(button_click)

# Start the turtle main loop
turtle.mainloop()
