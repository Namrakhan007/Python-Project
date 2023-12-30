import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
carManager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.up,"Up")
# screen.onkey(player.left,"Left")
# screen.onkey(player.right,"Right")
scoreboard.update()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.move_cars()
    for car in carManager.all_Cars:
        if car.distance(player) < 20:
            game_is_on= False
            scoreboard.update_game()

    if player.at_finish_line():
        player.go_at_start()
        carManager.level_up()
        scoreboard.increase_score()

screen.exitonclick()
