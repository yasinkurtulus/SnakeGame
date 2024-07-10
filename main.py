from turtle import Screen,Turtle
import  time

from food import Food
from score_board import ScoreBoard
from  snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
snake=Snake()
turtle=Turtle()
food=Food()
score_board=ScoreBoard()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_left, "Left")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.refresh()
        snake.extend()
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        game_is_on=False
        score_board.game_over()
    for i in snake.bodies[1:]:
        if snake.head.distance(i)<10:
            game_is_on=False
            score_board.game_over()




#end game
screen.exitonclick()