import turtle as trtl
import random as rand

#configuration stuff
walls = trtl.Turtle()
walls.speed(0) # go fast!
wallLength = 0 #changed due to adding the doors
pathWidth = 30 # will I need this???? And this is a guess
doorWidth = 25 

mazeRunner = trtl.Turtle(shape="square")
mazeRunner.turtlesize(0.3)

mazeRunner.color("blue")
mazeRunner.pencolor("red")
mazeRunner.hideturtle()


#functions
def drawBarrier(pathW):
  walls.left(90)
  walls.forward(pathW)
  walls.forward(-pathW)
  walls.right(90)

def drawDoor(doorW):
  walls.pu()
  walls.forward(doorW)
  walls.pd()

def moveRunner():
  mazeRunner.forward(5)

def runnerUp():
  mazeRunner.setheading(90)

def runnerLeft():
  mazeRunner.setheading(180)

def runnerRight():
  mazeRunner.setheading(0)

def runnerDown():
  mazeRunner.setheading(270)



#Do stuff here

#build the wall
for i in range(25):
  walls.left(90)
  
  #add doors and barriers
  if i > 6:
    doorSpot = rand.randint(0,10+wallLength-doorWidth)
    barrierSpot = rand.randint(0,10+wallLength-doorWidth)
    #check if barrier is at a door, retry if it is
    while barrierSpot > doorSpot and barrierSpot < (doorSpot+doorWidth):
        barrierSpot = rand.randint(0,10+wallLength-doorWidth)
    if barrierSpot <= doorSpot:
      walls.forward(barrierSpot) #go to the spot to start the door.
      drawBarrier(pathWidth)
      walls.forward(doorSpot-barrierSpot) # get to door spot after barrier
      drawDoor(doorWidth)
      walls.forward(10+wallLength-doorWidth-doorSpot)
    else: #doing door first
      walls.forward(doorSpot) # get to door spot after barrier
      drawDoor(doorWidth)
      walls.forward(barrierSpot-doorSpot) # get to barrier spot after door
      drawBarrier(pathWidth)
      walls.forward(10+wallLength-doorWidth-barrierSpot)
  #add Doors to Wall
  elif i > 1: #don't do this for the first wall segment
    doorSpot = rand.randint(0,10+wallLength-doorWidth)
    walls.forward(doorSpot) #go to the spot to start the door.
    drawDoor(doorWidth)
    walls.forward(10+wallLength-doorWidth-doorSpot)
  #just wall, no doors or barriers
  else:
    walls.forward(10) #each door is 10 pixels off
    walls.forward(wallLength)
  wallLength +=15

walls.hideturtle()

mazeRunner.showturtle()



wn = trtl.Screen()

wn.onkeypress(runnerUp, 'w')
wn.onkeypress(runnerLeft, 'a')
wn.onkeypress(runnerDown, 's')
wn.onkeypress(runnerRight, 'd')
wn.onkeypress(moveRunner, 'w')
wn.listen()

wn.mainloop()