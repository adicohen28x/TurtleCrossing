from calendar import c
import time
from turtle import Screen
from player import FINISH_LINE_Y, STARTING_POSITION, Player
from car_manager import MOVE_INCREMENT, STARTING_MOVE_DISTANCE, CarManager
from scoreboard import Scoreboard
from player import Player
from scoreboard import Scoreboard

scoreboard =Scoreboard ()
screen = Screen()
screen.setup(width=600, height=500)
screen.title("My Turtle Crossing Game")
screen.tracer(0)
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    
    # # end level
    if player.ycor() >= FINISH_LINE_Y:
        car_manager.level()
        scoreboard.update_score()
        car_manager.move_cars()
        player.goto(STARTING_POSITION)

    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
