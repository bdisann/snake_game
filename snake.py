from turtle import Turtle

SNAKES_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]

    def create_snakes(self):
        for position in SNAKES_POSITIONS:
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(position)
            self.snakes.append(snake)

    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            x_cor = self.snakes[snake - 1].xcor()
            y_cor = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(x_cor, y_cor)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
