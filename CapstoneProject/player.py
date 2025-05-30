from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.reset()
        self.setheading(90)
        self.speed(0)
        self.move_distance = MOVE_DISTANCE
    def move_up(self):
        self.forward(self.move_distance)

    def reset(self):
        self.goto(STARTING_POSITION)

    def is_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False



