import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Drawing Board")


turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_left():
    turtle_instance.setheading(turtle_instance.heading() - 10)
    #turtle_instance.left(10)

def rotate_right():
    turtle_instance.setheading(turtle_instance.heading() + 10)
    #turtle_instance.right(10)

def clear_screen():
    turtle_instance.clear()

def home_back():
    turtle_pen_up()
    turtle_instance.home()
    turtle_pen_down()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(turtle_forward, "space")
drawing_board.onkey(rotate_left, "Down")
drawing_board.onkey(rotate_right, "Up")
drawing_board.onkey(clear_screen, "c")
drawing_board.onkey(home_back, "h")

turtle.mainloop()