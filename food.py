from turtle import Turtle
import random

FOOD_SHAPE = "circle"
FOOD_SIZE_STRETCH = 0.5
FOOD_COLOR = "blue"
FOOD_SPEED = "fastest"
EDGE_BUFFER = 20

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=FOOD_SIZE_STRETCH, stretch_wid=FOOD_SIZE_STRETCH)
        self.color(FOOD_COLOR)
        self.speed(FOOD_SPEED)
        self.refresh()

    def refresh(self):
        x_limits = (int((-1 * SCREEN_WIDTH / 2) + EDGE_BUFFER), int((SCREEN_WIDTH / 2) - EDGE_BUFFER))
        y_limits = (int((-1 * SCREEN_HEIGHT / 2) + EDGE_BUFFER), int((SCREEN_HEIGHT / 2) - EDGE_BUFFER))

        random_x = random.randint(x_limits[0], x_limits[1])
        random_y = random.randint(y_limits[0], y_limits[1])

        self.goto(random_x, random_y)
