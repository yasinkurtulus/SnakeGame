from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,270)
        self.refresh()
    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 16, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=('Arial', 16, 'bold'))