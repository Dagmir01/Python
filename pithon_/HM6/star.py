import turtle

screen = turtle.Screen()
star = turtle.Turtle()

star.penup()
star.goto(-100, 0)
star.pendown()
star.speed(5) 

for n in range(9):
    star.forward(150) 
    star.right(200)

turtle.done()