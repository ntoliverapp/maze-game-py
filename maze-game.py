#Part 1: Setting up the Maze
import turtle
#create a window, turtle module, screen method
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('A Maze Game')
wn.setup(700, 700)

#Create Pen - a class defines an object. Object called pen is a child of the turtle modules Turtle class. Pen is a turtle. Class is not an object, a class defines an object. Whenever you use a class, you have to initialize it with __init__. Pen is a child of turtle class, so we have to initialize that class. .speed relates to animation speed (0 is the fastest). All turtles start their life at the center of the screen (0,0)
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)

#Create levels list - because we need to give the pen a place to go. Created a LIST called levels. 
levels = ['']

#Define first level - screen is blocks across and 20 blocks down. We can create levels by changing the text. X is wall (can use any character), space is hollow. 
level_1 = []
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXX          XXXXX",
"X  XXXXXXX"

    



