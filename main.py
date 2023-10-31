
#Turtle Party Project
# By PinkDragon94 - Cher Slaughter
import turtle

turtle.color("red")

# Function to move forward with penup and pendown
def forward(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

# Function to draw a square with a given size
def square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

# List of square sizes
square_sizes = [100, 75, 50,]

# Starting position
x, y = -150, 0

# Loop through the list of square sizes and draw the squares
for size in square_sizes:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    square(size)
    forward(size + 20)  # Adjust the forward distance to separate the squares
    x, y = turtle.pos()  # Update the current position
