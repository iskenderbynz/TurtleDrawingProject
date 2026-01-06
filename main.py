import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")


turtle_instance = turtle.Turtle()


#square
'''
turtle_instance.setx(150)
turtle_instance.sety(150)
turtle_instance.setx(0)
turtle_instance.sety(0)
'''

#star
'''
for i in range(5):
    #ilk 4 satır farklı bir yıldız cıkarmaktadır. Sonraki 2 satır ise farklı ayrı ayrı test edilebilir!
    turtle_instance.left(60)
    turtle_instance.forward(100)
    turtle_instance.right(120)
    turtle_instance.forward(100)
    turtle_instance.left(144)
    turtle_instance.forward(100)
'''

#polygon

num_sides = 6
angle=360.0/num_sides # *2 eklenir ise yıldız çizer.
side_length=100

for i in range(num_sides):
    turtle_instance.left(angle)
    turtle_instance.forward(side_length)


turtle.done()