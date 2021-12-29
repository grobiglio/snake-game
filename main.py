from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Guillermo's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    # Detect collision with the wall
    if (snake.head.xcor() > 280 or
            snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or
            snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # Detect collision with itself
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()