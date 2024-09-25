#Sean Kenneally
#23/9/24
#Learning Turtle

import turtle
turtle.shape("turtle")

#scr=turtle.Screen()
#scr.bgcolor("yellow")
#turtle.pensize(3)
#turtle.forward(20)
#turtle.penup()
#turtle.forward(20)
#turtle.pendown()
#turtle.color("green","brown")
#turtle.begin_fill()
#for i in range(0,4):
    #turtle.forward(100)
    #turtle.right(90)
#turtle.end_fill()

#scr=turtle.Screen()
#scr.bgcolor("red")
#for i in range (0,10):
    #turtle.color("blue","red")
    #turtle.right(36)
    #for i in range (0,5):
      #turtle.forward(100)
      #turtle.right(144)

#Challenge 5

#scr=turtle.Screen()
#scr.bgcolor("pink")
#turtle.color("green","red")
#turtle.pensize(5)

#for i in range(0,4):
    #turtle.forward(20)
    #turtle.penup()
    #turtle.forward(20)
    #turtle.pendown()
    #turtle.forward(20)
    #turtle.penup()
    #turtle.forward(20)
    #turtle.pendown()
    #turtle.forward(20)
    #turtle.right(90)


#Challenge 6
#turtle.color("blue","red")

#turtle.begin_fill()
#for i in range (0,3):
    #turtle.forward(50)
    #turtle.left(120)
    #turtle.end_fill()
    
#turtle.forward(50)
#turtle.penup()
#turtle.forward(20)
#turtle.pendown()

#turtle.color("red","red")

#for i in range (0,3):
    #turtle.forward(50)
    #turtle.left(120)
    
#turtle.forward(50)
#turtle.penup()
#turtle.forward(20)
#turtle.pendown()

#turtle.color("green","red")

#for i in range (0,3):
    #turtle.forward(50)
    #turtle.left(120)

#Challenge 7
import random
amount = random.randint(1,1000000)
line_length = random.randint(25,100)
colour = random.choice(["red","blue","green", "pink", "purple", "brown", "orange", "black", "yellow"])
angle = random.randint(1,360)

for i in range(amount):
    turtle.right(angle)
    turtle.forward(line_length)
    turtle.color(colour)


turtle.exitonclick()