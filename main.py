from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreBoard import Scoreboard

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Aryan's Snake Game")
screen.tracer(0)


# Function to start the game
def game_start():
    # Clear the start screen message
    homepage.clear()

    # Initialize game objects
    scoreboard = Scoreboard()
    snake = Snake()
    food = Food()

    # Set up controls
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    game_on = True
    count = 0
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision of head with the food
        if snake.head.distance(food) < 15:
            food.refresh()
            count += 1
            scoreboard.refresh(count)
            snake.extend()

        # Detect collision with the wall
        if (snake.head.xcor() > 295 or snake.head.xcor() < -295 or
                snake.head.ycor() > 295 or snake.head.ycor() < -295):
            game_on = False
            scoreboard.gameOver()

        # Detect collision with the snake's own body
        for segment in snake.segments:
            if segment != snake.head and segment.distance(snake.head) < 10:
                game_on = False
                scoreboard.gameOver()

    screen.bye()  # Close the window when the game is over


# Create and configure the start screen turtle
homepage = Turtle()
homepage.hideturtle()
homepage.penup()
homepage.pencolor("white")
style = ('Courier', 50, 'bold')
style2 = ('Courier', 19, 'bold')

# Display start screen text
homepage.goto(0, 0)
homepage.write('Snake Game!', font=style, align='center')
homepage.goto(0, -30)
homepage.write('Press Space to Play!', font=style2, align='center')
homepage.goto(0,-250)
homepage.write('By: Aryan Kumar ', font=style2, align='center')

# Bind the start function to the spacebar key
screen.listen()
screen.onkey(game_start, "space")

# Start the Turtle graphics loop
screen.mainloop()
