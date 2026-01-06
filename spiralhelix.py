import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Spiralhelix")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle_instance.speed(10)
turtle_colors = ["red","purple","green","yellow","blue","magenta"]

for i in range(15):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)



turtle.done()
