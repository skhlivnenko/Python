import turtle

def draw_romb (some_turtle):
    for i in range (0,2):
        some_turtle.forward(50)
        some_turtle.left(30)
        some_turtle.forward(50)
        some_turtle.left(150)
 
def draw_flower():
    window = turtle.Screen()
    window.bgcolor("red")

    romb = turtle.Turtle()
    romb.speed(20)
    romb.shape("turtle")

    for i in range (0,36):
        draw_romb(romb)
        romb.left(10)

    romb.right(90)
    romb.forward(200)

   #window.exitonclick()

draw_flower()
    
