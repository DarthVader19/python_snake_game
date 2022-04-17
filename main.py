# from tracemalloc import start
# import turtle  as t
# import random

# screen=t.Screen()
# screen.setup(600,600)
# def new_turt():
#     return t.Turtle()
# new=new_turt()
# list_turt=[]
# color=['white','red','blue']
# def rand_color():
#     return random.choice(color)
# pos=[(0,0),(-20,0),(-40,0)]
# screen.bgcolor('black')
# for n in range(3):
#     new=new_turt()
#     list_turt.append(new)
#     if n==0:
#       new.color('blue')
#     else:
#       new.color('white')
#     new.shape('square')
#     new.penup()
#     new.goto(pos[n])

# def  move_all():
   
#     for seg in range(len(list_turt)-1,0, -1):
#         new_x=list_turt[seg-1].xcor()
#         new_y=list_turt[seg-1].ycor()
        
#         list_turt[seg].goto(new_x,new_y)
#     list_turt[0].fd(20)
     

   
    
# screen.tracer(0)

# import  time    
# game_on=True

# while game_on:
#     screen.update()
#     move_all()
#     screen.onkey(turn_up,'Up')
#     screen.onkey(turn_down,'Down')
#     screen.onkey(turn_right,'Right')
#     screen.onkey(turn_left,'Left')


#     screen.listen()
#     time.sleep(0.5)
 
# screen.exitonclick()


# Using Classes 
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import random

SPEED=0.14  #in seconds 

COLOR=['blue','orange','white','cyan','green','violet']
screen=Screen()
def game():
    game_on=True
    
    my_snake=Snake()
    my_food=Food()
    score=Scoreboard()

    

    while game_on:
        score.welcome(random.choice(COLOR))
        my_snake.move()
        time.sleep(SPEED)
        # print(my_snake.snake_pos, my_food.food_pos)
        if my_food.food_pos==my_snake.snake_pos:
            my_snake.snake_len +=1
            my_food.hide_food()
            my_food.create_food()
            score.update_score()
            my_snake.increase_snake()

        my_snake.turn()
        # my_snake.boundary_teleport()
        game_on=my_snake.boundary_wall()

        for seg  in my_snake.segments[1:]:
           if my_snake.head.distance(seg)<10:
              game_on=False
              score.game_over()

    # my_snake.game_over()
    score.game_over()

    # detecting collision with itself
    
    
    start_game()

def start_game():
    # screen.bgpic("start.gif")
    # time.sleep(3)
    new_game=screen.textinput("Snake Game","Enter 'y' to play new game")

    if new_game.lower()=='y':
      screen.bgpic("nopic")
    #   screen.clear()
      game()
    else:
     screen.bye()

start_game()   







