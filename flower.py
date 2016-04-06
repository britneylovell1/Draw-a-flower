import turtle

window = turtle.Screen()

def draw_triangle(some_turtle):
    some_turtle.forward(28*3)
    some_turtle.right(180 - 67)
    some_turtle.forward(36*3)
    some_turtle.right(180 - 46)
    some_turtle.forward(36*3)
    some_turtle.right(180 - 67)

def draw_flower():
    audrey = turtle.Turtle()
    audrey.color('#ff3399')
    audrey.shape('turtle')
    
    for i in range(1,37):
        draw_triangle(audrey)
        audrey.right(10)
    
    audrey.right(90)
    audrey.forward(200)

draw_flower()
turtle.exitonclick()
