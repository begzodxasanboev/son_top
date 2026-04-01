import os
import turtle
os.system('cls')

turtle.speed(3)
turtle.pensize(5)
for i in range(10,500,10):
    turtle.right(90)
    turtle.forward(i)
turtle.done()