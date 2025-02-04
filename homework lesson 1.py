print ("andria patsatsia")

from turtle import*

#we want to paint a house
speed(7)
width(5)
color("teal")
forward (200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square
#making door
begin_fill()
forward(70)
left(90)
color("pink")
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("gold")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("brown")

penup()
goto(200, 110)
begin_fill()
left(30)
right(90)
forward(20)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


penup()
goto(0, 110)
left(90)
forward(20)
pendown()
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()







exitonclick()


   
