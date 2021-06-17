#Turtle Drawing Ver.1.0
#Written by Jiyeon Choi
#Jun.17.2021.

import turtle as t

#Turn right and go
def right():
    t.setheading(0)
    t.forward(5)


#Turn upward and go
def up():
    t.setheading(90)
    t.forward(5)


#Turn left and go
def left():
    t.setheading(180)
    t.forward(5)


#Turn downward and go
def down():
    t.setheading(270)
    t.forward(5)


#Turtle's tail up, unable drawing
def pen_up():
    t.penup()


#Turtle's tail down, enable drawing
def pen_down():
    t.pendown()


#Set window title
t.title("Turtle Drawing")

#Make turtle
t.shape("turtle")
t.color("teal")
t.pendown()

#Set speed
t.speed(0)

#Set pensize
t.pensize(3)
t.pencolor("darkblue")

#move the turtle by clicking the mouse
t.onscreenclick(t.goto)

#Set keyboard to make turtle move
t.onkeypress(right, "Right")
t.onkeypress(up, "Up")
t.onkeypress(left, "Left")
t.onkeypress(down, "Down")
t.onkeypress(pen_up, "space")
t.onkeypress(pen_down, "a")
t.listen()

t.mainloop()