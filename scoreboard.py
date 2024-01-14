from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="left", font=("Arieal", 50, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="right", font=("Arieal", 50, "normal"))

    def l_increase(self):
        self.l_score += 1

    def r_increase(self):
        self.r_score += 1




