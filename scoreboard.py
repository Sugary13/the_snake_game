from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.write(f"Score: {self.score}",  align="center", font=("Arial", 16, "bold"))
