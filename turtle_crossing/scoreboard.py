import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.timmy = turtle.Turtle()
        self.timmy.color("black")
        self.score = 0
        self.timmy.hideturtle()
        self.timmy.penup()
    def update(self):
        self.timmy.goto(-240,270)
        self.timmy.write(f"Score: {self.score}", align="center", font=("courier", 24, "normal"))


    def update_game(self):
         self.timmy.goto(0,0)
         self.timmy.write("GAME OVER", align="center", font=("courier", 24, "normal"))
    def increase_score(self):
        self.score +=1
        self.timmy.clear()
        self.update()

