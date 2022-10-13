#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0
# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("gray")
  y = y + 5 # location of next floor

  newBuilding = floor % 21
  if newBuilding == 20:
    x = x + 50
    y = -150
  
  rem = floor % 9
  if (rem > 2):
    painter.color("red")
  if (rem > 5):
    painter.color("pink")
  floor = floor + 1
 


  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()
