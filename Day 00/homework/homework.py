# DRAWING THE HOUSE

from turtle import *

# drawing the square
speed(50)
width(10)
color("pink")
forward(250)  
left(90)
forward(250)
left(90)
forward(250)
left(90)
forward(250)
left(90)

# drawing the door
forward(90)
color("green")
left(90)
begin_fill()
forward(90)
right(90)
forward(70)
right(90)
forward(90)
end_fill()

# drawing the roof
penup()
goto(250, 250)
pendown()
right(140)
color("blue")
begin_fill()
forward(200)
left(100)
forward(200)
end_fill()

# drawing the first window
penup()
goto(0, 250)
left(40)
color("brown")
begin_fill()
forward(60)
pendown()
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

# drawing the second window
penup()
goto(250, 130)
pendown()
begin_fill()
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()


exitonclick()