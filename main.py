import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkSeaGreen")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()



screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    scoreboard.update_highest_level()
    
    
    if player.ycor() > 265:
        scoreboard.point()
        player.reset_position()
        car_manager.win()
    
    
    for car in car_manager.all_cars:
        if car.distance(player) < 23:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
