from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

GAME_TIME_INCREMENT = 0.1

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20

X_UPPER = SCREEN_WIDTH / 2 - BLOCK_SIZE / 2
X_LOWER = -1 * SCREEN_WIDTH / 2 + 2
Y_UPPER = SCREEN_HEIGHT / 2 - 2
Y_LOWER = -1 * SCREEN_HEIGHT / 2 + BLOCK_SIZE / 2


UP_KEY = "Up"
DOWN_KEY = "Down"
LEFT_KEY = "Left"
RIGHT_KEY = "Right"
FOOD_COLLISION_DISTANCE = 15
SELF_COLLISION_DISTANCE = 10

# Initialise screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialise snake object
snake = Snake()

# Initialise food object
food = Food()

# Initialise scoreboard object
score_board = ScoreBoard()

# Caller the screen listening to register user key inputs and move snake accordingly
screen.listen()
screen.onkeypress(snake.up, key=UP_KEY)
screen.onkeypress(snake.down, key=DOWN_KEY)
screen.onkeypress(snake.left, key=LEFT_KEY)
screen.onkeypress(snake.right, key=RIGHT_KEY)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(GAME_TIME_INCREMENT)
    snake.move()

    # Detect collision with food.
    if snake.snake_head.distance(food) < FOOD_COLLISION_DISTANCE:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    # Detect collision with wall
    snake_x = snake.snake_head.xcor()
    snake_y = snake.snake_head.ycor()
    if snake_x > X_UPPER or snake_x < X_LOWER or snake_y > Y_UPPER or snake_y < Y_LOWER:
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.snake_head.distance(segment) < SELF_COLLISION_DISTANCE:
            score_board.reset()
            snake.reset()

screen.exitonclick()
