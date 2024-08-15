from turtle import Turtle
import os.path

HIGH_SCORE_FILE_NAME = "data.txt"

SCREEN_HEIGHT = 600
BUFFER_SIZE = 35

GAME_OVER_TEXT = "GAME OVER!"
COLOR = "white"
MOVE = False
ALIGN = "center"
FONT = ("Courier", 24, "bold")
SCOREBOARD_POS = (0, SCREEN_HEIGHT / 2 - BUFFER_SIZE)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.current_player_score = 0
        self.high_score = 0
        self.goto(x=SCOREBOARD_POS[0], y=SCOREBOARD_POS[1])
        self.extract_data()
        self.update_scoreboard()

    def reset(self):
        if self.current_player_score > self.high_score:
            self.high_score = self.current_player_score
            self.save_high_score()
        self.current_player_score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        score_text = f"{GAME_OVER_TEXT}"
        self.write(arg=score_text, move=MOVE, align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        score_text = f"Score: {self.current_player_score} High Score: {self.high_score}"
        self.write(arg=score_text, move=MOVE, align=ALIGN, font=FONT)

    def increase_score(self):
        self.current_player_score += 1
        self.update_scoreboard()

    def extract_data(self):
        if os.path.exists(HIGH_SCORE_FILE_NAME):
            self.read_file()
        else:
            self.save_high_score()

    def read_file(self):
        with open(HIGH_SCORE_FILE_NAME, mode="r") as file:
            file_data = file.read()
            if file_data != "":
                self.high_score = int(file_data)
            else:
                self.save_high_score()

    def save_high_score(self):
        with open(HIGH_SCORE_FILE_NAME, mode="w") as file:
            file.write(f"{self.high_score}")
