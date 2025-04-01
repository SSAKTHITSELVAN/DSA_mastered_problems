import turtle

def spiral(pen, llen):
    if llen >= 0:
        pen.forward(llen)
        pen.right(90)
        spiral(pen, llen-5)

pen = turtle.Turtle()
paper = turtle.Screen()
spiral(pen, 200)
paper.exitonclick()