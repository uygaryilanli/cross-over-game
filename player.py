from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 14
FINISH_LINE_Y = 280


class Player(Turtle):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.starting_pos = STARTING_POSITION
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(self.starting_pos)
        self.setheading(90)
    
    
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < FINISH_LINE_Y:
            self.sety(new_y)
    
    
    def reset_position(self):
        self.goto(self.starting_pos)
