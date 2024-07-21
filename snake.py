from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP= 90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments=[]
        self.createSnake()
        self.head=self.segments[0] #THIS IS THE OBJECT OF THE HEAD OF THE TURTLE

    def createSnake(self):
        for coordinates in STARTING_POSITIONS:
            self.add_segment(coordinates)

    def add_segment(self,coordinates):
        new_s = Turtle(shape="square")
        new_s.color("white")
        new_s.penup()
        new_s.goto(coordinates)
        self.segments.append(new_s)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            # THIS PART IS VERY IMPORTANT AND MUST BE UNDERSTOOD
            #THIS CODE MAKES THE SNAKE MOVE 1 STEP AT A TIME
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def up(self):
        if self.head.heading()!=DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.segments[0].setheading(DOWN)

