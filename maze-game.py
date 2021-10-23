#Part 1: Setting up the Maze
import turtle
import math
#create a window, turtle module, screen method
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('A Maze Game')
wn.setup(700, 700)

#Register shapes
turtle.register_shape('ninja_right.gif')
turtle.register_shape('ninja_left.gif')
turtle.register_shape('tree_one.gif')
turtle.register_shape('coin.gif')

#Create Pen - a class defines an object. Object called pen is a child of the turtle modules Turtle class. Pen is a turtle. Class is not an object, a class defines an object. Whenever you use a class, you have to initialize it with __init__. Pen is a child of turtle class, so we have to initialize that class. .speed relates to animation speed (0 is the fastest). All turtles start their life at the center of the screen (0,0)
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)

#create Player class
class Player(turtle.Turtle): #the player is a child of the turtle modules turtle class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('ninja_right.gif')
        self.color('blue')
        self.penup()
        self.speed(0)
        self.gold = 0
    def go_up(self): #Create player movement, adding it to player class. 
        #Calculate the next spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_down(self): 
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    def go_left(self): 
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        self.shape('ninja_left.gif')        
    def go_right(self): 
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        self.shape('ninja_right.gif')
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2)) #pythagorean theorem
    
        if distance < 5:
            return True
        else:
            return False
        
#Create Treasure class
class Treasure(turtle.Turtle): #the player is a child of the turtle modules turtle class
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('coin.gif')
        self.color('gold')
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
        
#Create levels list - because we need to give the pen a place to go. Created a LIST called levels. 
levels = ['']

#Define first level - screen is 25 columns and 25 rows of blocks (x and y coordinates). We can create levels by changing the text. X is wall (can use any character), space is for movement through maze. 
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X TXXX        XXXX TXXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX", 
"XXXXXXXXXXX      XXXXX TX",
"XXXXXXXXXXXXXX   XXXXX  X",
"XXX TXXXXXXXXX          X",
"XXX                     X",
"XXX            XXXXXXXXXX",
"XXXXXXXXXXX    XXXXXXXXXX",
"XXXXXXXXXXX             X",
"XX    XXXXX             X",
"XX    XXXXXXXXXXX   XXXXX",
"XX     XXXXXXXXXX   XXXXX",
"XXT         XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Add a treasures list #to collect treasures into the list over time#
treasures = []

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
                pen.shape('tree_one.gif')
                pen.stamp() #stamp the screen with a block/wall
                #Add coordinates to the wall list
                walls.append((screen_x, screen_y)) #double parenthesis is a tuple, append all coordinates (x and y) of every block in the walls
            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)
            #Check if it is a T (representing the treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y)) #x and y coordinates in Treasure class
                
#Create class instances 
pen = Pen()
player = Player() #the player is an instance of the player class

#Create wall coordinate list
walls = []

#Invoke the function
setup_maze(levels[1])
#print(walls)


#Keyboard Binding:
turtle.listen() #going to listen to the keyboard
turtle.onkey(player.go_left, "Left") #player comes from instance name, go_left comes from player function
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

#Turn off screen update
wn.tracer(0) #stops the animation for while loop

#Main Game Loop
while True:
    #check for player collision with treasure
    #iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #add the treasure gold to the player gold
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            #Destroy the treasure
            treasure.destroy()
            #remove the treasure from the treasures list
            treasures.remove(treasure)
    
    #Update Screen
    wn.update() #update window after the loop
    





