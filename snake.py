from turtle import Turtle
SNAKES_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:


    def __init__(self):
        self.snakes = []
        self.create_snakes()


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
