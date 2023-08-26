import turtle as t
def O12():
    t.speed(45)
    t.color("green")
    t.penup()
    t.goto(20,170)
    t.pendown()
    t.circle(15,600,100)

def O11():
    t.speed(45)
    t.color("blue")
    t.penup()
    t.goto(-80,160)
    t.pendown()
    t.circle(15,600,100)

def O13():
    t.speed(45)
    t.color("red")
    t.penup()
    t.goto(100,150)
    t.pendown()
    t.circle(15,600,100)


def O21():
    t.speed(45)
    t.color("yellow")
    t.penup()
    t.goto(-80,70)
    t.pendown()
    t.circle(15,600,100)


def O31(): 
    t.speed(45)
    t.color("purple")
    t.penup()
    t.goto(-80,10)
    t.pendown()
    t.circle(15,600,100)


def O22():
    t.speed(45)
    t.color("orange")
    t.penup()
    t.goto(10,70)
    t.pendown()
    t.circle(15,600,100)



def O23():
    t.speed(45)
    t.penup()
    t.goto(100,70)
    t.pendown()
    t.circle(15,600,100)



def O32():
    t.speed(45)
    t.penup()
    t.goto(20,10)
    t.pendown()
    t.circle(15,600,100)



def O33():
    t.penup()
    t.goto(100,10)
    t.pendown()
    t.circle(15,600,100)

if __name__=="__main__":
    O11()
    O12()
    O13()
    O21()
    O22()
    O23()
    O31()
    O32()
    O33()