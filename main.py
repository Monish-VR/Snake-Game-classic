from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Monish's   Snake   Game")
screen.listen()
snake = Snake()
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
food = Food()
score = ScoreBoard()
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -295:
        for i in snake.segments:
            i.goto(1000, 1000)
        snake.clr()
        score.high()
        snake.create()

    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 5:
            for i in snake.segments:
                i.goto(1000, 1000)
            snake.clr()
            score.high()
            snake.create()
    if snake.segments[0].distance(food) < 15:
        score.increase()
        food.refresh()
        snake.extend_snake()

screen.exitonclick()

