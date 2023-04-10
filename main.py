import turtle as t

kachva = t.Turtle()
screen = t.Screen()


def move_front():
    kachva.forward(10)


def move_back():
    kachva.backward(10)


def turn_left():
    kachva.right(10)
    # kachva.forward(50)


def turn_right():
    kachva.left(10)
    # kachva.forward(50)

def clear():
    kachva.clear()
    kachva.penup()
    kachva.home()
    kachva.pendown()


screen.listen()
screen.onkey(key="w", fun=move_front)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
