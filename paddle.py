from turtle import Turtle
# POSITION = (350,0)
class Paddle(Turtle) :
    def __init__(self,POSITION):
        super().__init__()
        self.create_paddle(POSITION)

    def create_paddle(self,POSITION) :
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(POSITION)

    def up(self):
        ypos = self.ycor()+20
        self.goto(self.xcor(),ypos)

    def down(self):
        ypos = self.ycor() - 20
        self.goto(self.xcor(), ypos)


