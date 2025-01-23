import turtle

def draw_heart():
    """Draw a heart shape using the turtle."""
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def write_message(message, x, y, font_size=24, font_type="bold"):
    """Write a message on the turtle screen."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.write(message, align="center", font=("Arial", font_size, font_type))

# Setup turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Proposal to Navya")

# Create a turtle instance
teja = turtle.Turtle()
teja.speed(5)

# Draw the heart
teja.penup()
teja.goto(0, -200)
teja.pendown()
draw_heart()

# Write the proposal
write_message("To Navya,", 0, 120, font_size=32)
write_message("i love you ma forever and ever ma ❤", 0, 70, font_size=26)
write_message("- From Teja", 0, 20, font_size=24)

# Keep the screen open
teja.hideturtle()
turtle.done()
