from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score={self.score}  High Score={self.high_score}", False, "center", ("Ariel", 20
                                                                                          , "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Data.txt" ,mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",False,"center",("Ariel",20,"normal"))
    def increment(self):
        self.score += 1
        self.clear()
        self.update_score()
