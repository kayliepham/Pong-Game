from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)


    def move_up(self):
        y_coordinate = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=y_coordinate)


    def move_down(self):
        y_coordinate = self.ycor() - MOVE_DISTANCE
        self.goto(x=self.xcor(), y=y_coordinate)

