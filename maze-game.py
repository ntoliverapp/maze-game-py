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

#create Player class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('blue')
        self.penup()
        self.speed(0)

#Create levels list - because we need to give the pen a place to go. Created a LIST called levels. 
levels = ['']

#Define first level - screen is 25 columns and 25 rows of blocks (x and y coordinates). We can create levels by changing the text. X is wall (can use any character), space is for movement through maze. 
level_1 = [
"X  XXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX", 
"XXXXXXXXXXX      XXXXX  X",
"XXXXXXXXXXXXXX   XXXXX  X",
"XXX  XXXXXXXXX          X",
"XXX                     X",
"XXX            XXXXXXXXXX",
"XXXXXXXXXXX    XXXXXXXXXX",
"XXXXXXXXXXX             X",
"XX    XXXXX             X",
"XX    XXXXXXXXXXX   XXXXX",
"XX     XXXXXXXXXX   XXXXX",
"XX          XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Append (add) maze to mazes list
levels.append(level_1)
    
#Create level set up FUNCTION - starts at first row, column (-288, 288). Then theres a nested loop. (each block is 24 wide)
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinate
            #NOTE the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            #Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y) #x, y, coordinates on the screen
                pen.stamp() #stamp the screen with a block/wall

#Create class instances 
pen = Pen()

#Invoke the function
setup_maze(levels[1])

while True:
    #pass
    wn.update()





