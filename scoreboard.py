from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_1, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.score_2, align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.score_1 += 1
        self.update()

    def r_point(self):
        self.score_2 += 1
        self.update()
