import turtle 
import random

class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #10 by 10 circle
        self.color("blue")
        self.speed("fastest")
        self.update_food()
    
    def update_food(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,265)
        self.goto(random_x, random_y)

