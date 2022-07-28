from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(100, 180)
        self.write(arg = f"{self.r_score}", align = "center", font = ("Arial", 80, "normal"))
        self.goto(-100, 180)
        self.write(arg = f"{self.l_score}", align = "center", font = ("Arial", 80, "normal"))


    def right_score(self):

        self.r_score += 1
        self.clear()
        self.update_scoreboard()



    def left_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

