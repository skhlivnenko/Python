import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.left(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create the Turtle brad - draw the square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(10)
    for i in range (0,36):
        draw_square(brad)
        brad.right(10)
    

draw_art ()
window.exitonclick()
    
