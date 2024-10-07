from turtle import Turtle

ALIGNMENT= "center"
FONT= ("Courier",15,"bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.pencolor("white")
        with open("data.txt") as data:
            self.highScore=int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def refresh(self,count):
        self.clear()
        self.score=count;
        self.write(f"Score: {count} High Score: {self.highScore}",align=ALIGNMENT,font=FONT)


    def reset(self):
        if(self.score>self.highScore):
            self.highScore=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highScore}")
        self.score=0
        self.refresh(self.score)