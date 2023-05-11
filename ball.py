from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.x_direction = 10
        self.y_direction = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce(self, direction):
        self.move_speed *= 0.8
        if direction == "y":
            self.y_direction *= -1
        elif direction == "x":
            self.x_direction *= -1
