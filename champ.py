from turtle import Turtle


class Champ(Turtle):
    def __init__(self):
        super().__init__()
        self.size=1 # size of padle
        self.coordinate_x = 0
        self.coordinate_y = -260
        self.initiate_object()

    def initiate_object(self):
        self.shapesize(self.size,5)
        self.shape("square")
        self.goto(self.coordinate_x,self.coordinate_y)
        self.color("white")
        self.penup()

    def change_position_left(self):
        self.coordinate_x -=20
        self.goto(self.coordinate_x,self.coordinate_y)

    def change_position_right(self):
        self.coordinate_x += 20
        self.goto(self.coordinate_x, self.coordinate_y)
