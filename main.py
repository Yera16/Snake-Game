from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("gray")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

still_playing = True
while still_playing:
    screen.update()
    time.sleep(0.12)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.change_score()

    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        scoreboard.game_reset()
        snake.reset()

    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.game_reset()
            snake.reset()








screen.exitonclick()