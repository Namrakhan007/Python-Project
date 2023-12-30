from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import scoreboared
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("MY_SNAKE_GAME")

screen.tracer(0)
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score = scoreboared()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision to food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    #detect collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on= False
        score.update_game()
    #tel collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_is_on = False
            score.update_game()

screen.exitonclick()
