from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
turtle = Turtle()
ball = Ball()


screen.bgcolor("black")
screen.title("PING PONG")
screen.setup(width=800, height=600)
screen.tracer(0)

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)
#
# screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))


screen.listen()
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")
screen.onkey(player_2.go_up, "w")
screen.onkey(player_2.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    ball.move()

screen.exitonclick()