import turtle

def tree_tree(n, pen):
    if n > 5:
        pen.forward(n)
        pen.right(20)
        tree_tree(n-15, pen)
        pen.left(40)
        pen.forward(n)
        tree_tree(n-15, pen)
        pen.backward(n)


pen = turtle.Turtle()
pen.left(90)
paper = turtle.Screen()
tree_tree(110, pen)
paper.exitonclick()
