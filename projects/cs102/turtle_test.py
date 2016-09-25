import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    yogi = turtle.Turtle
    yogi.color("red")
    yogi.speed(5)
    yogi.forward(100)
    yogi.right(90)
    yogi.forward(100)
    yogi.right(90)
    yogi.forward(100)
    yogi.right(90)
    yogi.forward(100)
    yogi.right(90)
    
    
    window.exitonclick()

draw_square()
