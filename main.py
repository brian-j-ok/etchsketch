from turtle import Turtle, Screen

screen = Screen()
cursor = Turtle()


def move_forward():
    cursor.forward(10)

def move_backward():
    cursor.back(10)

def turn_left():
    cursor.left(10)

def turn_right():
    cursor.right(10)

def clear():
    cursor.clear()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
