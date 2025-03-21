import turtle

def tree(t, branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(t, branch_len-15)
        t.left(40)
        tree(t, branch_len-15)
        t.right(20)
        t.backward(branch_len)

my_turtle = turtle.Turtle()
my_win  = turtle.Screen()
my_turtle.left(90)
my_turtle.up()
my_turtle.backward(200)
my_turtle.down()
my_turtle.color("black")
tree(my_turtle, 110)
my_win.exitonclick()