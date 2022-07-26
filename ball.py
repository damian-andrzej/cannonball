from turtle import Turtle
import time
import tkinter as tk
from tkinter import ttk

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.size1 = 1
        self.size2 = 1
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.3
        self.origin_location = (0,0)
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.shapesize(stretch_wid=self.size1, stretch_len=self.size2)
        self.goto(self.origin_location)
        self.color("blue")
        self.penup()


    def move(self):
        #time.sleep(self.speed)
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)
        time.sleep(0.01)
        #self.after(30,self.move)

    def bounce(self):
        self.x_move *= -1

    def bounce_block(self):
        self.y_move *= -1
        self.speed *= 0.8

    def reset(self):
        time.sleep(0.5)
        self.x_move *= -1
        self.goto(self.origin_location)
        self.speed = 0.1