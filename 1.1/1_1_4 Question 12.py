#   a114_nested_loops_2.py
import turtle as trtl

color1 = "orange"
color2 = "purple"
color3 = "cyan"
color4 = "red"
wn = trtl.Screen()
width = 400
height = 300

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

answer = "y"
while (answer == "y"):
  wn.clearscreen()  
  painter.goto(0,0)
  space = 1

  angle = int(input("angle:"))
  seg = int(360/angle)
  while painter.ycor() < height:
      if (space%200==0):
          painter.fillcolor(color4)
          painter.color(color4)
      elif (space % 100 == 0): 
          painter.fillcolor(color3)
          painter.color(color3)
      painter.right(angle)
      painter.forward(2 * space + 10) # experiment
      painter.begin_fill()
      painter.circle(3)
      painter.end_fill()
      space = space + 1
  answer = input("again?")
