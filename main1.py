#polygon function 
import turtle

turtle.color("red")

# Function to move forward with penup and pendown
def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

# Function to draw a square with a given size
def polygon(num, size):
    for _ in range(num):
        turtle.forward(size)
        turtle.left(360 / num)

polygon(4, 100)
back(125)
polygon(3, 50)
