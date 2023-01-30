from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)



    def move(self):
        self.setheading(35)
        self.forward(20)
