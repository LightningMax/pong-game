from turtle import Turtle
import time

INITIAL_PLAYER_POSITION = [(-260, -20), (-260, 0), (-260, 20)]
INITIAL_ENEMY_POSITION = [(260, -20), (260, 0), (260, 20)]


class Paddle():
    def __init__(self, position):
        self.body = []
        self.position = position
        self.create_paddle()
        self.head = self.body[2]
        self.tail = self.body[0]
        self.length = len(self.body)
        
    def create_paddle(self):
        for position in self.position:
            square = Turtle("square")
            square.penup()
            square.color("white")
            square.goto(position)
            self.body.append(square)

    def up(self):
        for square in self.body:
            square.sety(square.ycor() + 20)

    def down(self):
        for square in self.body:
            square.sety(square.ycor() - 20)


class EnemyPaddle(Paddle):
    def __init__(self):
        super().__init__()
        