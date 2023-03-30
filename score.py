import turtle
POS = "center"
STYLE = ('Arial', 15, 'normal')

with open("score.txt") as file:
    high_score = int(file.read())

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score = high_score
        self.goto(0, 275)
        self.color("white")
        self.writescore()
       
    def writescore(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}",align=POS, font= STYLE)

    def score_update(self):
        self.score += 1
        self.writescore()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.writescore()