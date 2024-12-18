from turtle import Screen
from cars import Car
import time
from timmy import Tim
from scoreboard import Speed

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("road crossing")
screen.tracer(0)
car=Car()
timmy=Tim()
speed=Speed()
screen.listen()
screen.onkey(timmy.tim_up,"Up")

game_on=True
while game_on:
        time.sleep(0.1)
        screen.update()

        car.car_move()
        car.car_reset()
        for contact in car.segments:
                if contact.distance(timmy)<20:
                        speed.lose()
                        game_on=False
        if timmy.ycor()>280:
                timmy.win_sit()
                car.x_move=4
                car.car_move()
                speed.speed_update()

screen.exitonclick()