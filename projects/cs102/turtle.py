import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(1)
    
    brad.foward(100)
    print ("Step one")
    brad.right(90)
    brad.foward(100)
    print ("Step two")
    brad.right(90)
    brad.foward(100)
    print ("Step three")
    brad.right(90)
    brad.foward(100)    
    print ("Last step")

    window.exitonclick()

draw_square()