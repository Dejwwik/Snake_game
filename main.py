import turtle
import time
import snake
import food
import score

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("Snake game")
screen.tracer(0)

my_snake = snake.Snake()
my_food = food.Food()
my_score = score.Score()

screen.listen()
screen.onkey(fun=my_snake.up, key="Up")
screen.onkey(fun=my_snake.down, key="Down")
screen.onkey(fun=my_snake.left, key="Left")
screen.onkey(fun=my_snake.right, key="Right")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.12)
    my_snake.move()

    if my_snake.head.distance(my_food) < 15:
        my_food.update_food()
        my_snake.extend()
        my_score.score_update()
    
    #collision with wall
    if my_snake.head.xcor() < -297 or my_snake.head.xcor() > 297 or my_snake.head.ycor() < -297 or my_snake.head.ycor() > 297:
        my_score.reset()
        my_snake.snake_reset()

    #collision with tail
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 3:
            my_score.reset() 
            my_snake.snake_reset()

screen.exitonclick()
