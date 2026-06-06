import turtle
turtle.Screen().bgcolor("orange")

sc=turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    i=i+1