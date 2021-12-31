from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('blank') # self.hideturtle() es otra opción válida
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        score_text = (
            f"Score: {self.score} "
            f"High score: {self.high_score}"
        )
        self.write(score_text,
                   align=ALIGNMENT,
                   font=FONT)

    def increase(self):
        self.score += 1
        self.update_scoreboard()
        

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        with open('data.txt') as data:
            self.high_score = int(data.read())

    def write_high_score(self):
        with open('data.txt', 'w') as data:
            data.write(str(self.high_score)) 

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)