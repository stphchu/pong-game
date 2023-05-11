from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.pu()
        self.setpos(x, y)
        self.seth(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.shape("square")
        self.color("white")

    def move_up(self):
        if self.ycor() <= 200:
            self.fd(40)

    def move_down(self):
        if self.ycor() >= -200:
            self.bk(40)
