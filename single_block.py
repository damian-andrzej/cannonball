from turtle import Turtle

class Single_block(Turtle):
    def __init__(self,position_x,position_y):
        super().__init__()
        self.coordinate_x = position_x
        self.coordinate_y = position_y
        self.size = 1
        self.size_y = 2
        self.create_blocks()

    def create_blocks(self):
        self.shape("square")
        self.shapesize(self.size,self.size_y)
        self.goto(self.coordinate_x,self.coordinate_y)
        self.color("white")
        self.penup()
