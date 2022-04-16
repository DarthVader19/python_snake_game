from  turtle import Turtle,Screen
screen_=Screen()

STARTING_POS=[(0,0),(-20,0),(-40,0)]

class Snake:


    def __init__(self) :
        self.screen=screen_
        self.screen.reset()

        self.snake_len=3
        self.snake_pos=(0,0)
        self.updated_pos=[]
        self.segments=[]
        self.create_snake(STARTING_POS)
        self.screen.setup(600,600)
        self.screen.tracer(0)
        self.screen.bgcolor('black')
    
    def create_snake(self,pos):
        for n in range(self.snake_len):
            new=Turtle()
            self.segments.append(new)
            if n==0:
             new.color('blue')
            else:
             new.color('white')
            new.shape('square')
            new.penup()
            new.goto(pos[n])
    

    


    def increase_snake(self):
        # print(self.snake_len)
        
        new=Turtle()
        new.color('white')
        new.penup()
        new.shape('square')
        self.segments.append(new)
        

        
        


    def move(self):
        self.screen.update()
        for seg in range(len(self.segments)-1,0, -1):
            
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        
        self.segments[0].fd(20)
        x,y=self.segments[0].pos()
        x=round(x)
        y=round(y)
        self.snake_pos=(x,y)
    
    def turn(self):
        self.screen.listen()
        self.screen.onkey(self.turn_up,'Up')
        self.screen.onkey(self.turn_down,'Down')
        self.screen.onkey(self.turn_right,'Right')
        self.screen.onkey(self.turn_left,'Left')


    def turn_up(self):
    
        self.segments[0].setheading(90)

    def turn_down(self):
    
        self.segments[0].setheading(270)

    def turn_left(self):
        # list_turt[0].left(90)
        self.segments[0].setheading(180)

    def turn_right(self):
        self.segments[0].setheading(0)
    
    

    def boundary_wall(self):
        x,y=self.snake_pos
        print(x,y)
        if x==300 or x==-300 or y==300 or y==-300:
            return False
        else:
            return True



    def boundary_teleport(self):
        x_pos, y_pos=self.snake_pos
        x_pos=round(x_pos)
        y_pos=round(y_pos)
        if x_pos==300 or x_pos==-300:
            
            self.segments[0].goto(-x_pos,y_pos)
        if int(y_pos)==300 or int(y_pos)==-300:
            print(y_pos)
            self.segments[0].goto(x_pos,-y_pos)

    def game_over(self):
        
        self.screen.bgpic('giphy.gif')
        
               
