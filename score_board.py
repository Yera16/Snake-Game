from turtle import Turtle
import time
ALIGNMENT = "center"
FONT = ("Courier", 17, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open ("data.txt") as data:
            self.highest_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=365)
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highest score: {self.highest_score}",align = ALIGNMENT, font=FONT)
        with open("data.txt", mode="w") as data:
            data.write(f"{self.highest_score}")

    def game_reset(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)
        self.screen.update()
        time.sleep(2)
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.clear()
        self.score = 0
        self.goto(x=0, y=365)
        self.write_score()

    def change_score(self):
        self.score += 1
        self.write_score()


