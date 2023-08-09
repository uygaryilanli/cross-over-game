from turtle import Turtle


FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        with open("!!!BULUNDUĞUNUZ DOSYA KONUMUNU GİRİN!!!/data.txt") as data:
            self.highest_level_score = int(data.read())
        self.update_score()
    
    
    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Level: {self.level} | Highest Level: {self.highest_level_score}", align="center", font=FONT)
    
    
    def point(self):
        self.level += 1
        self.update_score()
    
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
    
    
    def update_highest_level(self):
        if self.level > self.highest_level_score:
            self.highest_level_score = self.level
            with open("!!!BULUNDUĞUNUZ DOSYA KONUMUNU GİRİN!!!/data.txt", mode="w") as data:
                data.write(f"{self.highest_level_score}")
                data.close()
