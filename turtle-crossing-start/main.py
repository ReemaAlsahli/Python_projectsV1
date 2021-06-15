import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if player.ycor() > 280:
        player.refresh()
        score.level_incrase()
        car_manager.move_incresa()

    for car in car_manager.all_car:
        if player.distance(car) < 30:
            game_is_on = False
            score.game_over()


screen.exitonclick()