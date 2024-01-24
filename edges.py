from turtle import Turtle

class Edge_1(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=1, stretch_len=100)
        self.penup()
        self.goto(position)

class Edge_2(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=1, stretch_len=100)
        self.penup()
        self.goto(position)