from turtle import Turtle

USER_POSITION = [(-470, 40), (-470, 20), (-470, 0), (-470, 20), (-470, 40)]
COMP_POSITION = [(460, 40), (460, 20), (460, 0), (460, 20), (460, 40)]
moving_forward = False


class Pong:

    def __init__(self):
        super().__init__()
        self.pong_bar_user = []
        self.pong_bar_comp = []
        self.computer_score = 0
        self.user_score = 0
        self.ball = Turtle()
        self.direction_right = False
        self.score_board_text = Turtle()
        self.go_text = Turtle()

    def segment(self, position, list_name, color):
        """This is the function to create a block for our pong bar, it takes three attributes
           1st position of our segment
           2nd list to append our segments to create a bar
           3rd is the color of bar
        """
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color(color)
        new_segment.goto(position)
        list_name.append(new_segment)

    def bar(self, position_list, list_for_segment, color):
        """It is function to create a bar from segments with help of segment function
           1st position of our segment
           2nd list in which append our segments to create a bar
           3rd is the color of bar
        """
        for i in range(5):
            self.segment(position_list[i], list_for_segment, color=color)

    def user_bar(self):
        """ It is  a user bar creating function"""
        self.bar(USER_POSITION, list_for_segment=self.pong_bar_user, color="blue")

    def computer_bar(self):
        """It is a computer bar creating function"""
        self.bar(COMP_POSITION, list_for_segment=self.pong_bar_comp, color="red")

    def line_in_center(self):
        """It is used to create a center line for our pong game."""
        line = Turtle()
        line.hideturtle()
        line.penup()
        line.setheading(-90)
        line.color("white")
        line.goto(x=0, y=290)
        line.pensize(5)
        while line.ycor() > -290:
            line.pendown()
            line.forward(20)
            line.penup()
            line.forward(20)

    def move_comp_bar(self):
        """This function help our computer bar to move in y-coordinates of screen."""
        global moving_forward
        if self.pong_bar_comp[0].ycor() == 280:
            moving_forward = False
        elif self.pong_bar_comp[-1].ycor() < -210:
            moving_forward = True

        for i in range(len(self.pong_bar_comp)):
            self.pong_bar_comp[i].setheading(90)
            if moving_forward:
                self.pong_bar_comp[i].forward(40)
            else:
                self.pong_bar_comp[i].backward(40)

    def create_ball(self):
        """This function help to create a ball."""
        self.ball.penup()
        self.ball.color("white")
        self.ball.shape("square")

    def ball_move(self):
        """This function help to move ball across the screen"""
        self.ball.backward(20)

    def ball_touch_user_bar(self, list_name, angle):
        """This function is used to check the ball is touched with user bar, if touch then change the heading of our ball
            It takes two attributes
            1. List of user bar
            2. angle on which you want to tilt.
            and return us direction is right.
        """
        for i in range(4):
            if list_name[i].distance(self.ball) < 20:
                self.ball.setheading(angle)
                self.direction_right = True
                return self.direction_right

    def ball_touch_comp_bar(self, list_name, angle):
        """This function is used to check the ball is touched with user bar, if touch then change the heading of our ball
                   It takes two attributes
                   1. List of user bar
                   2. angle on which you want to tilt.
                   and return us direction is not right.
               """
        for i in range(4):
            if list_name[i].distance(self.ball) < 20:
                self.ball.setheading(angle)
                self.direction_right = False
                return self.direction_right

    def move_user_bar_upward(self):
        """It moves our bar in positive x-coordinate."""
        for i in range(len(self.pong_bar_user)):
            self.pong_bar_user[i].setheading(90)
            self.pong_bar_user[i].forward(10)

    def move_user_bar_downward(self):
        """It moves our bar in negative x-coordinate."""
        for i in range(len(self.pong_bar_user)):
            self.pong_bar_user[i].setheading(90)
            self.pong_bar_user[i].backward(10)

    def game_over(self):
        """It creates a game over text."""
        self.go_text.hideturtle()
        self.go_text.color("white")
        self.go_text.write("Game Over", align='center', font=('Arial', 48))

    def clear_game_over(self):
        """It clears the game over text """
        self.go_text.clear()

    def score_board(self):
        """It creates a score board on  screen and show the score of user and computer."""
        self.score_board_text.color("white")
        self.score_board_text.penup()
        self.score_board_text.hideturtle()
        self.score_board_text.goto(0, 230)
        self.score_board_text.write(f"{self.user_score}      {self.computer_score}", align='center', font=('Arial', 48))

    def clear_score_board(self):
        """It deletes the score board."""
        self.score_board_text.clear()

    def instruction_line(self):
        """To show some instructions text."""
        instruction_text = Turtle()
        instruction_text.color("white")
        instruction_text.hideturtle()
        instruction_text.penup()
        instruction_text.goto(-480, -280)
        instruction_text.write("To exit the game, Press 'Esc' key on your key board", font=('Arial', 12))
