from turtle import Turtle

ALIGNMENT= "center"
FONT= ("Courier",15,"bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def refresh(self,count):
        self.clear()
        self.write(f"Score: {count}",align=ALIGNMENT,font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER!!", align=ALIGNMENT, font=FONT)