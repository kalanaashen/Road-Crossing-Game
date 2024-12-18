from turtle import Turtle

class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.left(90)
        self.goto(0,-250)

    def tim_up(self):
        self.forward(20)

    def win_sit(self):
        self.goto(0,-250)

