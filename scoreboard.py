from turtle import Turtle
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-210,220)
        self.leveli = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.leveli +=1 
        self.write(f"Level:{self.leveli}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=FONT)
