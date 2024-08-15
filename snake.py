from turtle import Turtle

MOVE_DISTANCE = 20
UP_HEADING = 90
LEFT_HEADING = 180
RIGHT_HEADING = 0
DOWN_HEADING = 270

DISPOSE_BLOCKS_POS = (1000, 1000)


class Snake:

    def __init__(self):
        self.block_size = 20
        self.initial_block_number = 3
        self.snake_segments = []
        self.snake_shape = "square"
        self.snake_color = "White"
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for i in range(0, self.initial_block_number):
            y_pos = 0
            x_pos = 0 + -1 * self.block_size * i
            position = (x_pos, y_pos)
            self.add_segment(position)

    def add_segment(self, position):
        body_block = Turtle(shape=self.snake_shape)
        body_block.color(self.snake_color)
        body_block.penup()
        body_block.goto(position)
        self.snake_segments.append(body_block)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x_pos = self.snake_segments[seg_num - 1].xcor()
            new_y_pos = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x=new_x_pos, y=new_y_pos)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN_HEADING:
            self.snake_head.setheading(UP_HEADING)

    def down(self):
        if self.snake_head.heading() != UP_HEADING:
            self.snake_head.setheading(DOWN_HEADING)

    def left(self):
        if self.snake_head.heading() != RIGHT_HEADING:
            self.snake_head.setheading(LEFT_HEADING)

    def right(self):
        if self.snake_head.heading() != LEFT_HEADING:
            self.snake_head.setheading(RIGHT_HEADING)

    def reset(self):
        for segment in self.snake_segments:
            segment.goto(DISPOSE_BLOCKS_POS)
        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]
