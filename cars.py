import random
from turtle import Turtle,Screen
COLORS=["red","purple","cornflower blue","coral","spring green","blue violet","indigo","light coral","gold","light cyan"]

screen=Screen()
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.segments=[]
        self.create_cars()
        self.x_move=1


    def create_cars(self):
        for car in range(20):
            car=Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.setheading(180)
            car.goto(300+(random.randrange(100,1000,50)), random.randrange(-230, 230,10))
            self.segments.append(car)


    def car_move(self):
        for car in range(len(self.segments)):
            self.segments[car].forward(random.randrange(1,10)+self.x_move)


    def car_reset(self):
        if self.segments[19].xcor()<-320:
            for car in range(20):
                screen.tracer(0)
                self.segments[car].goto(random.randrange(400,1000,50),self.segments[car].ycor())
                screen.update()
                self.car_move()