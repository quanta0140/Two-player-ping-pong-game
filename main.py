from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG GAME")

screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score = ScoreBoard()




screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
# ball.refresh((380,290))

game = True
while game :
    time.sleep(0.1)
    screen.update()
# Detect collision with wall
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

# Detect collision with right paddle
    if ball.xcor()>330 and ball.distance(r_paddle)<50 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.bounce_x()

    # If r_paddle misses ball
    if ball.xcor()>380 :
        ball.goto(0,0)
        ball.bounce_x()
        score.l_increase()
        score.update()

    # If l_paddle misses ball
    if ball.xcor()<-380:
        ball.goto(0, 0)
        ball.bounce_x()
        score.r_increase()
        score.update()




screen.exitonclick()