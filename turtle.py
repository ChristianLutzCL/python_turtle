import turtle

my_turtle = turtle.Turtle()

def square_circ(n):
	for i in range(n):
		square()
		my_turtle.right(11)

def square():
	for i in range(4):
		my_turtle.forward(100)
		my_turtle.right(90)



def circle():
    for i in range(500):
        my_turtle.speed(0)
        my_turtle.circle(100)
        my_turtle.left(11)
        my_turtle.color('red', 'yellow')
        my_turtle.begin_fill()

    my_turtle.end_fill()

#heheeheh
#jojojo
square_circ(500)
