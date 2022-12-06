from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        with open("data.txt") as file:
            content = file.read()
        self.high_score = int(content)
        self.color("white")
        self.hideturtle()
        self.clear()
        self.write(f"Score: {self.score} HighScore : {self.high_score}", align="center", font=("Arial", 18, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} HighScore : {self.high_score}", align="center", font=("Arial", 18, "normal"))

    def high(self):
        if self.high_score < self.score:
            self.high_score = self.score
        with open("data.txt", "w") as file:
            content = file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}   HighScore : {self.high_score}", align="center", font=("Arial", 18, "normal"))

