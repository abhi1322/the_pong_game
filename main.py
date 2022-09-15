from turtle import Screen, bye
from pong import Pong
import time


def close_game():
    """ To shut down the game window."""
    bye()


# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.tracer(0)
pong = Pong()

# setup game components like ball, user bar, computer bar and line in centr
pong.user_bar()
pong.computer_bar()
pong.line_in_center()
pong.create_ball()
is_game_on = True
screen.listen()

# Adding on key press functionality
screen.onkey(fun=pong.move_user_bar_upward, key="Up")
screen.onkey(fun=pong.move_user_bar_downward, key="Down")
screen.onkey(fun=close_game, key="Escape")
pong.ball.speed("fastest")


while is_game_on:
    screen.update()
    time.sleep(0.1)
    pong.score_board()
    pong.move_comp_bar()
    user = pong.ball_touch_user_bar(pong.pong_bar_user, 145)
    comp = pong.ball_touch_comp_bar(pong.pong_bar_comp, 325)
    pong.instruction_line()

    # Check ball direction and bounce back from side walls
    if pong.ball.ycor() > 200 and not pong.direction_right:
        pong.ball.setheading(30)
    elif pong.ball.ycor() < -200 and not pong.direction_right:
        pong.ball.setheading(-30)
    elif pong.ball.ycor() > 200:
        pong.ball.setheading(145)
    elif pong.ball.ycor() < -200:
        pong.ball.setheading(220)

    # Check ball missed by comp or user, if miss update score or else move ball.
    if pong.ball.xcor() > 480:
        pong.game_over()
        pong.user_score += 1
        pong.ball.goto(0, 0)
        pong.ball.setheading(0)
        time.sleep(1)
        pong.clear_game_over()
        pong.clear_score_board()
    elif pong.ball.xcor() < -480:
        pong.game_over()
        pong.computer_score += 1
        pong.ball.goto(0, 0)
        pong.ball.setheading(0)
        time.sleep(1)
        pong.clear_game_over()
        pong.clear_score_board()
    else:
        pong.ball_move()

screen.exitonclick()
