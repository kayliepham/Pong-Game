from turtle import Turtle

STARTING_POSITION = (0, 0)
STARTING_SPEED = 0.1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(45)
        self.move_speed = STARTING_SPEED


    def move(self):
        self.forward(25)

    def bounce_wall(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def bounce_paddle(self):
        new_heading = 180 - self.heading()
        self.setheading(new_heading)

    def reset_position(self, heading):
        self.goto(STARTING_POSITION)
        self.setheading(heading)