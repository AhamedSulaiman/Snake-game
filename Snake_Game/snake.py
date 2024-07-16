from turtle import Turtle
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.snake_pos=[(0,0),(-20,0),(-40,0)]
        self.seg=[]
        self.create_snake()
        self.head = self.seg[0]

    def create_snake(self):
        for i in self.snake_pos:
            self.add_seg(i)

    def add_seg(self,i):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(i)
        self.seg.append(tim)

    def extend(self):
        self.add_seg(self.seg[-1].position())

    def reset(self):
        for i in self.seg:
            i.goto(1000,1000)
        self.seg.clear()
        self.create_snake()
        self.head=self.seg[0]
    def move(self):
        for i in range(len(self.seg)-1,0,-1):
            new_x=self.seg[i-1].xcor()
            new_y=self.seg[i-1].ycor()
            self.seg[i].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)