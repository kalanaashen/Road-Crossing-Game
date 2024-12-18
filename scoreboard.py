from turtle import Turtle

class Speed(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-30, 200)
        self.hideturtle()
        self.color("white")
        self.speed = 0
        self.speed_board()

    def speed_board(self):
        self.write(f"SPEED:{self.speed}", False, "right", font=("arial", 20, "normal"))

    def speed_update(self):
        self.speed+=1
        self.clear()
        self.write(f"SPEED:{self.speed}", False, "right", font=("arial", 20, "normal"))


    def lose(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER", False, "center", font=("arial", 10, "normal"))