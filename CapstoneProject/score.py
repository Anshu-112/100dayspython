from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.hideturtle()
        self.penup()
        
        self.goto(-250,250)
        self.update_score()
       
       
        
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=("Arial",20,"normal"))
    def increase_score(self):
        self.score += 1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over" , align="center", font=("Arial",20,"normal"))



       

        