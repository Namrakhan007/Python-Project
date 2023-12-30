from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_Cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance ==1:
            carry = Turtle("square")
            carry.shapesize(stretch_wid=1,stretch_len=2)

            carry.color(random.choice(COLORS))
            carry.penup()
            random_y = random.randint(-250,250)
            carry.goto(300,random_y)
            self.all_Cars.append(carry)
    def move_cars(self):
        for car in self.all_Cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed +=MOVE_INCREMENT

