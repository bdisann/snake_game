from turtle import Screen, Turtle
from snake import Snake
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Python Snake Game")
screen.tracer(0)


snake = Snake()


screen.update()


snake_is_on = True
while snake_is_on:
    screen.update()

    snake.move()






screen.exitonclick()