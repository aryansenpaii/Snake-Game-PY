from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreBoard import Scoreboard

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Aryan's Snake Game")
screen.tracer(0)

scoreboard=Scoreboard()
snake=Snake()
food= Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")





game_on=True
count=0 # used to store the score in this locally
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detecting the collision of head with the food
    if(snake.head.distance(food)<15):

        food.refresh()
        count+=1
        scoreboard.refresh(count)
        snake.extend()

    #detecting collision with the wall
    if(snake.head.xcor()>295 or snake.head.xcor()<-295 or snake.head.ycor()>295 or snake.head.ycor()<-295):
        scoreboard.reset()
        snake.resetSnake()
        count=0

    #code to detect if the snake head is touching the body of the snake and trigger game over if so
    for segment in snake.segments:
        if(segment==snake.head):
            pass
        elif(segment.distance(snake.head)<10):
            scoreboard.reset()
            snake.resetSnake()
            count=0

screen.exitonclick()