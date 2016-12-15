import turtle
import math

bob = turtle.Turtle()

def arc(haustier, radius, angle):
	
	ecken = 180
	circumference = 2 * math.pi * radius
	length = circumference / ecken

	for i in range(ecken * angle/360):
		bob.fd(length)
		bob.lt(360/ecken)


arc(haustier = bob, radius = 50, angle = 180)


turtle.mainloop()


