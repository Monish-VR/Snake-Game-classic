from turtle import Turtle
Position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create()

    def create(self):
        for i in range(3):
            snake = Turtle()
            snake.penup()
            snake.shape("square")
            snake.pencolor("white")
            snake.fillcolor("white")
            snake.goto(Position[i])
            self.segments.append(snake)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.segments[0].forward(10)

    def extend_snake(self):
        end = self.segments[len(self.segments)-1]
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.pencolor("white")
        snake.fillcolor("white")
        self.segments.append(snake)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def clr(self):
        self.segments.clear()


