from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        

    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"Score: {self.score}", align="center", font=("Arial",20,"normal"))
        self.goto(100,200)
        self.write(f"Score: {self.score}", align="center", font=("Arial",20,"normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()
    def r_point(self):
        self.r_score += 1
        self.update_score()
