import turtle 
import time
FORVARD = 20
ANGLE = 90

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
  
    def create_snake(self):
        for index in range (3):
            segment = turtle.Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(x= -index *20, y= 0)
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1 ,0,-1):
            x_cord = self.segments[i-1].xcor()
            y_cord = self.segments[i-1].ycor()
            self.segments[i].goto(x_cord, y_cord)
        
        self.head.forward(FORVARD)   


    #defining move functions, blocking to turn 180 degress
    def left(self):
        heading = self.head.heading()
        if heading != 180 and heading != 0:
            self.head.setheading(180)

    def right(self):
        heading = self.head.heading()
        if heading != 0 and heading != 180:
            self.head.setheading(0)
        
    def up(self):
        heading = self.head.heading()
        if heading != 90 and heading != 270:
            self.head.setheading(90)

    def down(self):
        heading = self.head.heading()
        if heading != 270 and heading != 90:
            self.head.setheading(270)

    def snake_reset(self):
        for segment in self.segments:
            segment.hideturtle()  
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):

        new_segment = turtle.Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")    
        xcord = self.segments[len(self.segments) - 1].xcor()
        ycord = self.segments[len(self.segments) - 1].ycor()
        new_segment.goto(xcord, ycord)
        self.segments.append(new_segment)
