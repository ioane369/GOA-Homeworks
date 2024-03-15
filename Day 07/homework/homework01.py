# drawing a castle with a queen and a king

from turtle import *

speed(5000)

# DRAWING THE CASTLE

# drawing the first tower 
penup()
goto(-600, -300)
pendown()

width(6)

color("grey")

begin_fill()

forward(700)
left(90)
forward(500)
left(90)
forward(150)
left(90)
forward(500)

end_fill()

# drawing the roof for the first tower
penup()
goto(100, 200)
pendown()

color("red")

begin_fill()

left(90)
forward(30)
left(135)
forward(150)
left(90)
forward(150)
left(135)
forward(30)

end_fill()

# drawing the second tower

penup()
goto(-600, -300)
pendown()

color("grey")

begin_fill()

left(90)
forward(500)
right(90)
forward(150)
right(90)
forward(500)

end_fill()

# drawing the roof for the second tower
penup()
goto(-450, 200)
pendown()

color("red")

begin_fill()

left(90)
forward(30)
left(135)
forward(150)
left(90)
forward(150)
left(135)
forward(30)

end_fill()

# drawing the battlements
penup()
goto(-450, 0)
pendown()

color("black")

begin_fill()

forward(400)

left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)

right(90)
forward(40)
right(90)
forward(55)
left(90)
forward(60)
left(90)
forward(55)

right(90)
forward(40)
right(90)
forward(55)
left(90)
forward(60)
left(90)
forward(55)

right(90)
forward(40)
right(90)
forward(55)
left(90)
forward(60)
left(90)
forward(55)

right(90)
forward(40)
right(90)
forward(60)
left(90)
forward(30)

end_fill()

# drawing the third tower
penup()
goto(-145, 55)
pendown()

color("grey")

begin_fill()

right(90)
forward(200)
left(90)
forward(210)
left(90)
forward(200)

end_fill()

# drawing the roof for the third tower
penup()
goto(-145, 255)
pendown()

color("red")

begin_fill()

left(90)
forward(40)
left(135)
forward(210)
left(90)
forward(210)
left(135)
forward(45)

end_fill()

# drawing the window for the first tower
penup()
goto(55, 100)
pendown()

color("white")

begin_fill()

left(90)
forward(65)
left(90)
forward(55)
left(90)
forward(65)
left(90)
forward(55)

end_fill()

# drawing the window for the second tower
penup()
goto(-495, 100)
pendown()

begin_fill()

left(90)
forward(65)
left(90)
forward(55)
left(90)
forward(65)
left(90)
forward(55)

end_fill()

# drawing the window for the third tower
penup()
goto(-215, 210)
pendown()

begin_fill()

left(180)
forward(70)
left(90)
forward(80)
left(90)
forward(70)
left(90)
forward(80)

end_fill()

# drawing the door for castle
penup()
goto(-300, -300)
pendown()

color("brown")

begin_fill()

forward(200)
right(90)
forward(100)
right(90)
forward(200)

right(90)
forward(50)
right(90)

end_fill()

color("black")

forward(200)  


# DRAWING THE KING

#drawing the first boot
penup()
goto(200, -300)
pendown()

color("brown")

width(3)

begin_fill()

left(90)
forward(10)
right(90)
forward(10)
right(90)
forward(15)
left(90)
forward(20)
right(90)
forward(15)
right(90)
forward(30)
right(90)
forward(25)

end_fill()

penup()
goto(205, -270)
pendown()

color("black")

begin_fill()

forward(6)
right(90)
forward(10)
right(90)
forward(28)
right(90)
forward(10)
right(90)
forward(10)

end_fill()

#drawing the second boot
penup()
goto(250, -300)
pendown()

color("brown")

begin_fill()

right(90)
forward(30)
right(90)
forward(15)
right(90)
forward(20)
left(90)
forward(15)
right(90)
forward(10)
right(90)
forward(30)

end_fill()

penup()
goto(250, -270)
pendown()

color("black")

begin_fill()

forward(6)
right(90)
forward(10)
right(90)
forward(28)
right(90)
forward(10)
right(90)
forward(10)

end_fill()

# drawing the pants
penup()
goto(203, -260)
pendown()

color("chocolate")

begin_fill()

right(90)
forward(40)
right(90)
forward(65)
right(90)
forward(40)

right(90)
forward(20)
right(90)
forward(20)
left(90)
forward(24)
left(90)
forward(20)

end_fill()

# drawing the sweater
penup()
goto(203, -220)
pendown()

color("turquoise")

begin_fill()
right(90)
forward(7)
right(90)
forward(60)

left(140)
forward(40)
right(90)
forward(20)
right(90)
forward(60)

right(25)
forward(20)
right(25)
forward(50)
right(25)
forward(70)
right(90)
forward(20)
right(80)
forward(45)
left(105)
forward(61)
right(90)
forward(7)

end_fill()

# drawing the head
color("brown")

penup()
goto(233, -100)
pendown()

right(180)
circle(28)

# drawing the neck
penup()
goto(225, -122)
pendown()

left(90)
forward(25)

penup()
goto(245, -122)
pendown()

forward(25)

# drawing the crown
penup()
goto(233, -45)
pendown()

color("yellow")

begin_fill()

left(90)
forward(25)
right(90)
forward(25)
right(135)
forward(18)
left(90)
forward(18)
right(90)
forward(18)
left(90)
forward(18)
right(135)
forward(25)
right(90)
forward(25)

end_fill()

# drawing the first eye
penup()
goto(245, -63)
pendown()

color("black")

begin_fill()

circle(3)

end_fill()

# drawing the second eye
penup()
goto(220, -63)
pendown()

begin_fill()

circle(3)

end_fill()

# drawing the mouth
penup()
goto(240, -90)
pendown()

color("brown")
forward(10)
right(20)
forward(10)

penup()
goto(240, -90)
pendown()

right(140)
forward(10)

# drawing the first ear
penup()
goto(260, -70)
pendown()

color("brown")

left(40)
forward(10)
right(150)
forward(20)
right(90)
forward(7)

#drawing the second ear
penup()
goto(204, -70)
pendown()

right(60)
forward(10)
left(160)
forward(20)
left(90)
forward(7)

# drawing the nose
penup()
goto(237, -75)
pendown()

color("brown")

right(180)
forward(6)
left(30)
forward(2)

# drawing the first hand
penup()
goto(155, -180)
pendown()

color("brown")

forward(5)
left(90)
forward(3)
left(90)
forward(6)
left(180)
forward(8)
left(90)
forward(3)
left(90)
forward(9)
left(180)
forward(9)
left(90)
forward(3)
left(90)
forward(10)
left(180)
forward(7)
left(90)
forward(3)
left(90)
forward(8)
left(180)
forward(4)
left(90)
forward(3)
left(90)
forward(5)

# drawing the second hand
penup()
goto(320, -170)
pendown()

color("brown")

right(75)
forward(4)
left(90)
forward(3)
left(90)
forward(5)
right(180)
forward(7)
left(90)
forward(3)
left(90)
forward(8)
right(180)
forward(9)
left(90)
forward(3)
left(90)
forward(10)
right(180)
forward(8)
left(90)
forward(3)
left(90)
forward(9)
right(180)
forward(5)
left(90)
forward(3)
left(90)
forward(6)


# DRAWING THE QUEEN

# drawing the first foot
penup()
goto(450, -300)
pendown()

color("brown")


right(55)
forward(24)

penup()
goto(450, -300)
pendown()

right(90)
forward(15)
left(90)
forward(20)

# drawing the second foot
penup()
goto(500, -300)
pendown()

forward(20)

penup()
goto(500, -300)
pendown()

right(90)
forward(15)
left(90)
forward(24)

# drawing the dress
penup()
goto(465, -280)
pendown()

color("pink")

begin_fill()

right(90)
forward(35)
left(15)
forward(100)

end_fill()

penup()
goto(465, -280)
pendown()

begin_fill()

left(150)
forward(100)

right(110)
forward(140)

left(150)
forward(80)
right(90)
forward(20)
right(90)
forward(80)

left(10)
forward(20)
right(35)
forward(50)
right(25)
forward(100)
right(105)
forward(20)
right(70)
forward(90)

left(150)
forward(150)

end_fill()

# drawing the neck
penup()
goto(470, -110)
pendown()

color("brown")

left(140)
forward(20)

penup()
goto(490, -110)
pendown()

forward(22)

# drawing the head
penup()
goto(478, -88)
pendown()

right(90)
circle(28)

# drawing the crown
penup()
goto(478, -33)
pendown()

color("yellow")

begin_fill()

left(180)
forward(25)
right(90)
forward(25)
right(135)
forward(18)
left(90)
forward(18)
right(90)
forward(18)
left(90)
forward(18)
right(135)
forward(25)
right(90)
forward(25)

end_fill()

# drawing the first eye
penup()
goto(490, -51)
pendown()

color("black")

begin_fill()

circle(3)

end_fill()

# drawing the second eye
penup()
goto(465, -51)
pendown()

begin_fill()

circle(3)

end_fill()

# drawing the mouth
penup()
goto(485, -78)
pendown()

color("brown")

forward(10)
right(20)
forward(10)

penup()
goto(485, -78)
pendown()

right(140)
forward(10)

# drawing the first ear
penup()
goto(505, -58)
pendown()

left(40)
forward(10)
right(150)
forward(20)
right(90)
forward(7)

# drawing the second ear
penup()
goto(449, -58)
pendown()

right(60)
forward(10)
left(160)
forward(20)
left(90)
forward(7)

# drawing the nose
penup()
goto(482, -63)
pendown()

right(180)
forward(6)
left(30)
forward(2)

#drawing ehe first hand

penup()
goto(370, -157)
pendown()

forward(10)
left(90)
forward(3)
left(90)
forward(6)
left(180)
forward(8)
left(90)
forward(3)
left(90)
forward(9)
left(180)
forward(9)
left(90)
forward(3)
left(90)
forward(10)
left(180)
forward(7)
left(90)
forward(3)
left(90)
forward(8)
left(180)
forward(4)
left(90)
forward(3)
left(90)
forward(5)

# drawing the second hand
penup()
goto(585, -165)
pendown()

right(90)
forward(4)
left(90)
forward(3)
left(90)
forward(5)
right(180)
forward(7)
left(90)
forward(3)
left(90)
forward(8)
right(180)
forward(9)
left(90)
forward(3)
left(90)
forward(10)
right(180)
forward(8)
left(90)
forward(3)
left(90)
forward(9)
right(180)
forward(5)
left(90)
forward(3)
left(90)
forward(6)

# drawing the hair

penup()
goto(467, -33)
pendown()

color("violet")

left(55)
forward(15)
left(45)
forward(20)
left(50)
forward(53)
left(70)
forward(20)

penup()
goto(497, -33)
pendown()

forward(15)
right(35)
forward(20)
right(50)
forward(53)
right(80)
forward(30)

# drawing the grass
penup()
goto(-800, -302)
pendown()

color("green")

right(185)
forward(1600)


# COLORING THE LOWER PART OF THE CASTLE
penup()
goto(-450, -300)
pendown()

color("grey")

begin_fill()

left(90)
forward(300)
right(90)
forward(400)
right(90)
forward(300)
right(90)
forward(150)
right(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200)
right(90)
forward(150)

end_fill()


# COLORING THE LOWER PART OF THE THIRD TOWER
penup()
goto(-180, 55)
pendown()

color("grey")

begin_fill()

left(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)

end_fill()


# COLORING THE GRASS
penup()
goto(-800, -302)
pendown()

color("green")

begin_fill()

right(90)
forward(1600)
right(90)
forward(300)
right(90)
forward(1600)
right(90)
forward(300)

end_fill()



exitonclick()