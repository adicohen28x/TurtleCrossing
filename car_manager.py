from hashlib import new
from turtle import Turtle, TurtleScreen, colormode
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.leveli = STARTING_MOVE_DISTANCE 

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_c = Turtle()
            new_c.penup()
            new_c.shape("square")
            new_c.shapesize(stretch_wid=1, stretch_len=2)
            new_c.color(random.choice(COLORS))
            y = random.randint(-200,200)
            new_c.goto(300, y)
            self.cars.append(new_c)



    def move_cars(self):
        for car in range (len(self.cars)):
            x = self.cars[car].xcor() - self.leveli
            y = self.cars[car].ycor()
            self.cars[car].goto(x,y)
            
    
    def level(self):
        self.leveli+=STARTING_MOVE_DISTANCE
        for car in range (len(self.cars)):
            x = random.randint(5,270)
            y = self.cars[car].ycor()
            self.cars[car].goto(x,y)
        self.move_cars()
    
