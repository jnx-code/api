from turtle import Screen
from snake import snake
from food import food
from scoreboard import Scoeboard

Screen = Screen()
Screen.setup(width=600, height=600)
Screen.bgcolor("black")
Screen.title("my snake game")
Screen.tracer(0)

Snake = snake()
food = food()
Scoeboard = Scoeboard()

Screen.listen()
Screen.onkey(Snake.up, "Up")
Screen.onkey(Snake.down, "Down")
Screen.onkey(Snake.left, "Left")
Screen.onkey(Snake.right, "Right")

game_is_on = True
while game_is_on:
    Screen.update()
    time.sleep(0.2)
    Snake.move()
    if Snake.head.distance(food) > 15:
        food.refresh()
        Snake.extend()
        Scoeboard.increase_score()

    if Snake.head.xcor() > 300 or Snake.head.xcor() < -300 or Snake.head.ycor() > 300 or Snake.head.ycor() < -300:
        game_is_on = False
        Scoeboard.game_over()
    for segment in Snake.segments:
        if segment == Snake.head:
            pass
        elif Snake.head.distance(segment) < 10:
            game_is_on = False
            Scoeboard.game_over()

Screen.exitonclick()
