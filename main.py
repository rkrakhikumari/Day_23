from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import *
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

s = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

    if s.head.distance(food) < 15:
        food.refresh()
        s.extend()
        score.increase_score()

    if s.head.xcor() >290 or s.head.xcor() < -290 or s.head.ycor() > 290 or s.head.ycor() < -290:
        game_is_on = False
        Scoreboard.game_over()

    for segment in s.snakes[1:]:
        if s.head.distance(segment) < 10:
            game_is_on = False
            Scoreboard.game_over()


    
screen.exitonclick()
