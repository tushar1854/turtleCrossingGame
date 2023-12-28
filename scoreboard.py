from turtle import Turtle


FONT = {"Courier", 24, "normal"}


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 0

    def update_score(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.score}", align="center",
                   font=("Courier", 24, "normal"))

    def increase_score(self):

        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center",
                   font=("Courier", 24, "normal"))
