#by mschro67

from random import randint
from display import GridDisplay

g=GridDisplay(10, 10)

def reset():
    g.reset()

class GameOfLifeGrid():
    def __init__(self,width,heigth):
        self.grid=[[randint(0,1) for x in range(width)] for y in range(heigth)]
        self.gen=0
    
    def setGrid(self,grid):
        self.grid=grid.copy()
    
    def display(self):
        global g
        g.grid=self.grid.copy()
        g.width=len(self.grid[0])
        g.height=len(self.grid)
        g.display()
    
    def nextGen(self):
        self.gen+=1
        self.nextGrid=[[0 for x in range(len(self.grid[0]))] for y in range(len(self.grid))]
        self.alive=0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                neighbors=0
                for x in range(-1,2,1):
                    for y in range(-1,2,1):
                        try:
                            if self.grid[row+y][col+x]==1 and not (x==0 and y==0):
                                neighbors+=1
                        except:
                            pass
                if self.grid[row][col]==1:
                    if neighbors == 2 or neighbors == 3:
                        self.nextGrid[row][col]=1
                        self.alive+=1
                elif self.grid[row][col]==0 and neighbors==3:
                    self.nextGrid[row][col]=1
                    self.alive+=1
        self.grid=self.nextGrid.copy()
        if self.alive==0:
            return 0
        return 1