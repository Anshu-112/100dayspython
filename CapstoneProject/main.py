import time
from turtle import Screen
from player import Player
from car import CarManager
from score import Score

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

player=Player()
car = CarManager()
score = Score()

screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    # if player reach the end of the screen without collision
    if player.ycor() > 280:
        score.increase_score()
        player.goto(0,-280)
# collision with car

    for each_car in car.all_cars:
        if player.distance(each_car) < 20 :
            game_is_on = False
            score.game_over()

# collision with border
    if player.is_finish():
        player.reset()
        car.level_up()
        score.increase_score()




screen.exitonclick()

