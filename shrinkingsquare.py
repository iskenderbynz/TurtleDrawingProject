import turtle



turtle_screen = turtle.Screen()
turtle_screen.bgcolor("lightgreen")
turtle_screen.title("Shrinking Square")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 2
        print(size)
        if i==3:
            if int(size)>0:
                shrinkingSquare(size)

shrinkingSquare(150)
turtle.done()