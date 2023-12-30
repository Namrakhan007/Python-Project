from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

UP = 90
RIGHT = 0
LEFT = 180

class Player(Turtle):
     def __init__(self):
         super().__init__()
         self.shape("turtle")
         self.color("black")
         self.speed("fastest")

         self.setheading(90)
         self.penup()
         self.go_at_start()
     def up(self):
         new_y = self.ycor()+MOVE_DISTANCE
         self.goto(self.xcor(),new_y)
     def go_at_start(self):
         self.goto(STARTING_POSITION)

     def at_finish_line(self):
         if self.ycor() > FINISH_LINE_Y:
             return True
         else:
             return False
