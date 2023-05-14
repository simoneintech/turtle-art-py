import turtle 
from turtle import *

wn = turtle.Screen()

simone = turtle.Turtle()
colors = ['red', 'dark red']

def fleur():
    for i in range(300):
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)
        

fleur()
mainloop() 
turtle.done()
