from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)
    
    def extend(self):
        self.add_segment(self.snakes[-1].position())


    def move(self):
        for snak in range(len(self.snakes)-1 , 0, -1):
            new_x = self.snakes[snak - 1].xcor()
            new_y = self.snakes[snak - 1].ycor()
            self.snakes[snak].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snakes[0].setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

