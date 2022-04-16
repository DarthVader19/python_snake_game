
from turtle import Turtle, Screen
import random
from snake import screen_


tim=Turtle()
tim.hideturtle()

#Screen width and height
Width=300      
Height=300


class Food:

    def __init__(self):
        self.food_pos=(0,0)
        self.screen=screen_
        
        self.screen.update()
        self.create_food()
    
    def create_food(self):
        tim.penup()
        tim.color('red')
        self.food_pos=self.rand_pos()
        tim.goto(self.food_pos)
        tim.dot(10)
    
    def hide_food(self):
        tim.clear()


    def rand_pos(self):
        x=random.randint(-14,14)*20
        y=random.randint(-14,14)*20
        return (x,y)
        
    
        