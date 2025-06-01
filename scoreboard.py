from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def restart_text(self):
        self.goto(0, -30)
        self.write("Press 'r' to restart.", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

