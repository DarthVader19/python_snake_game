
from turtle import Turtle
welcome=Turtle()

FONT=('courier',20,'normal')
WELCOME_TEXT="Snake Game"

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.score=-1
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update_score()
       
    def update_score(self):
         self.score+=1
         self.clear()
         self.goto((0,260))
         self.write(f"Score = {self.score}",move=False,align="center", font=FONT)
    
    def welcome(self,color):
        welcome.penup()
        welcome.hideturtle() 
        welcome.goto(-270,260)
        welcome.pencolor(color)
        welcome.write(WELCOME_TEXT,True,align='left',font=('Arial',25))
        welcome.circle(30,180) 
    
    def game_over(self):
        
        self.screen.bgpic('giphy.gif')