import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(1)

    i=0
    while (i<4): 
        brad.forward(100)
        brad.right(90)
        i = i +1

    

def draw_circle():
    angie = turtle.Turtle()
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    tom = turtle.Turtle()

    for i in range (0,3):
        tom.forward(150)
        tom.left(120)
        
window = turtle.Screen()
window.bgcolor("red")
    
for i in range (0,36):
    draw_square ()
    brad.left(10)

#draw_circle ()
#draw_triangle()

window.exitonclick()
    
