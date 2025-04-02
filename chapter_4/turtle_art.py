import turtle
def spiral(pen, llen, res):
    if llen >= 0:
        pen.forward(llen)
        pen.right(90)
        res.append(spiral(pen, llen-5, res))

pen = turtle.Turtle()
paper = turtle.Screen()
res = []
spiral(pen, 100, res)
print(res)
print(len(res))
paper.exitonclick()
