from turtle import Turtle

class Snake:

    def __init__(self):
        self.snakes_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snakes = []

        for position in self.snakes_positions:
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
        self.snakes[0].forward(20)
