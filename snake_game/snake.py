from turtle import Turtle
segment_position = [(0, 0), (-20, 0), (-40, 0)]
distanceMoved = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in segment_position:
            self.add_segment(position)

    def add_segment(self,position):
        same = Turtle("circle")
        same.color("white")
        same.penup()
        same.goto(position)
        self.segments.append(same)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(distanceMoved)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)
