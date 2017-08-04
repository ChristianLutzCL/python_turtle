import turtle
import random

my_turtle = turtle.Turtle()

def square_circ(n):
	for i in range(n):
		my_turtle.color(random.choice(['brown', 'green', 'red', 'orange', 'blue', 'yellow', 'black', 'pink', 'grey', 'silver']))
		square(100)
		my_turtle.right(11)

def random_circ(n):
	for i in range(n):
		my_turtle.color(random.choice(['brown', 'green', 'red', 'orange', 'blue', 'yellow', 'black', 'pink', 'grey', 'silver']))
		square(random.randrange(10, 200))
		my_turtle.right(11)

def square(b):
	for i in range(4):
		my_turtle.forward(b)
		my_turtle.right(90)

def circle():
    for i in range(500):
        my_turtle.speed(0)
        my_turtle.circle(100)
        my_turtle.left(11)
        my_turtle.color('red', 'yellow')
        my_turtle.begin_fill()

def turn():
	my_turtle.left(180)



#square_circ(500)
