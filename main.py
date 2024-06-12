import random
import time
from turtle import Screen
from paddle import Paddle


INITIAL_PLAYER_POSITION = [(-260, -20), (-260, 0), (-260, 20)]
INITIAL_ENEMY_POSITION = [(260, -20), (260, 0), (260, 20)]


TOP_BORDER = 280
BOTTOM_BORDER = -280
GO_UP = True
GO_DOWN = False


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle(INITIAL_PLAYER_POSITION)
enemy_paddle = Paddle(INITIAL_ENEMY_POSITION)

screen.onkeypress(paddle.up ,"Up")
screen.onkeypress(paddle.down ,"Down")
screen.listen()


def detect_wall():
    if paddle.head.ycor() > TOP_BORDER:
        distance = TOP_BORDER
        for square in range(0, paddle.length):
            paddle.body[square].sety(distance)
            distance-=20
    
    if paddle.tail.ycor() < BOTTOM_BORDER:
        distance = BOTTOM_BORDER
        for square in range(0, paddle.length):
            paddle.body[square].sety(distance)
            distance+=20


def enemy_move():
    for square in enemy_paddle.body:
        time.sleep(0.005)
        square.forward(20)


def enemy_collision():
    global GO_UP
    global GO_DOWN

    if GO_UP:
        for square in enemy_paddle.body:
            square.setheading(90)

    if GO_DOWN:
        for square in enemy_paddle.body:
            square.setheading(270)

    if enemy_paddle.head.ycor() > TOP_BORDER:
        GO_UP = False
        GO_DOWN = True
    
    if enemy_paddle.head.ycor() < BOTTOM_BORDER:
        GO_UP = True
        GO_DOWN = False


game_over = False
while not game_over:
    screen.update()
    detect_wall()
    enemy_collision()
    enemy_move()
        
    


screen.exitonclick()