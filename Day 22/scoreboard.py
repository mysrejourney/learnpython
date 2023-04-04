from turtle import Turtle

ALIGNMENT='center'
FONT = ("Arial", 30,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Score : {self.left_score}", align=ALIGNMENT, font= FONT)
        self.goto(100, 250)
        self.write(f"Score : {self.right_score}", align=ALIGNMENT, font= FONT)

    def left_update_score(self):
        self.left_score += 1
        self.update_score()

    def right_update_score(self):
        self.right_score += 1
        self.update_score()