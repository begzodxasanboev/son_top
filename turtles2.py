import turtle

oyna = turtle.Screen()
oyna.bgcolor("black") 
oyna.title("Ajoyib Spiral")

chiziq = turtle.Turtle()
chiziq.speed(0) 
chiziq.pensize(4)

ranglar = ["red", "blue", "green", "yellow", "purple", "orange"]

for i in range(10, 500): 
    chiziq.color(ranglar[i % 5]) 
    chiziq.forward(i / 5)       
    chiziq.left(20)             

turtle.done()