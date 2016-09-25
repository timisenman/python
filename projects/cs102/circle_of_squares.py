#A Circle of Squares

#Either creates a draw square function,
#and rotate it 10 degrees 36 times.

import turtle

def draw_square(a_turtle):
    for i in range(1,5):
        a_turtle.forward(100)
        a_turtle.right(90)

def draw_art():

    window = turtle.Screen()
    window.bgcolor("blue")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(10)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    brad.right(630)
    print("Square done")
    
##    angie = turtle.Turtle()
##    angie.shape("turtle")
##    angie.color("yellow")
##    angie.speed(2)
##    angie.circle(100)
##    print("Circle drawn")
##
##    bro = turtle.Turtle()
##    bro.shape("turtle")
##    bro.color("green")
##    bro.speed(2)
##    bro.left(90)
##    bro.forward(100)
##    bro.left(90)
##    bro.forward(100)
##    bro.left(135)
##    bro.forward(141.42)
##    print("Triangle done")

    window.exitonclick()
    
draw_art()
