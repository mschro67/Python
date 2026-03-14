from turtle import *
from time import sleep

class GridDisplay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.t = Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.previous=[[]]

    def reset(self):
        self.previous=[[]]

    def display(self):
        self.t.clear()
        self.t.penup()
        self.t.goto(-400,-400)
        self.t.color("grey")
        for y in range(len(self.previous)):
            for x in range(len(self.previous[y])):
                if self.previous[y][x] == 1:
                    self.t.penup()
                    self.t.goto(x * 800 / len(self.previous[y]) -400, y * 800 / len(self.previous) -400)
                    self.t.pendown()
                    self.t.begin_fill()
                    for z in range(2):
                        self.t.forward(800 / len(self.previous[y]))
                        self.t.right(90)
                        self.t.forward(800 / len(self.previous))
                        self.t.right(90)
                    self.t.end_fill()

        self.t.color("black")
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 1:
                    self.t.penup()
                    self.t.goto(x * 800 / len(self.grid[y]) -400, y * 800 / len(self.grid) -400)
                    self.t.pendown()
                    self.t.begin_fill()
                    for z in range(2):
                        self.t.forward(800 / len(self.grid[y]))
                        self.t.right(90)
                        self.t.forward(800 / len(self.grid))
                        self.t.right(90)
                    self.t.end_fill()