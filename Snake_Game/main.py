from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
Screen().bgcolor("black")
Screen().setup(width=600,height=600)
Screen().title("Snake Game")
Screen().tracer(0)
score=ScoreBoard()

snake=Snake()
f1=Food()
Screen().listen()
Screen().onkey(snake.up,"Up")
Screen().onkey(snake.down,"Down")
Screen().onkey(snake.left,"Left")
Screen().onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    Screen().update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(f1)<15:
        f1.refresh()
        score.increment()
        snake.extend()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.reset()
        snake.reset()

    for i in snake.seg[1:]:
        if snake.head.distance(i) <10:
            score.reset()
            snake.reset()



Screen().exitonclick()