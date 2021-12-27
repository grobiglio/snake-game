from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('blank') # self.hideturtle() es otra opción válida
        self.goto(0, 270)
        self.color("white")
        self.score = -1
        self.increase()

    def increase(self):
        self.score += 1
        score_text = f"Score: {self.score}"
        self.clear()
        self.write(score_text,
                   align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)