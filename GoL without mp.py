import matplotlib as mpl 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import multiprocessing as mp

0
def initGrids(size):
    a = np.zeros((size, size), dtype = int)
    return a

def initCellsAlive(Grid):
    currentGrid = Grid
    cellCount = len(Grid[0])
    amountOfStartingPts = int(len(Grid)*len(Grid)*0.2)
    for i in range(amountOfStartingPts):
        xAxis = random.randrange(0, cellCount)
        yAxis = random.randrange(0, cellCount)
        currentGrid[xAxis, yAxis] = 1
    return currentGrid

def checkNeighbours(fps, Grid, img):
    currentGrid = Grid
    updatedGrid = np.zeros(currentGrid.shape, dtype=int)
    for row, col in np.ndindex(Grid.shape):
        numOfNbs = np.sum(currentGrid[row - 1:row+ 2, col - 1:col + 2], initial=0) - currentGrid[row][col]         
        if(numOfNbs < 0):
            numOfNbs = 0
        updatedGrid[row][col] = numOfNbs
    NbrMask = updatedGrid
    newGrid = np.zeros(Grid.shape, dtype=int)

    for row, col in np.ndindex(currentGrid.shape):
        if(currentGrid[row][col] == 1):
            if(NbrMask[row][col] < 2 or NbrMask[row][col] > 3):
                newGrid[row][col] == 0
            elif(NbrMask[row][col] == 2 or NbrMask[row][col] == 3):
                newGrid[row][col] = 1            
        if(currentGrid[row][col] == 0):
            if(NbrMask[row][col] == 3):
                newGrid[row][col] = 1

    img.set_data(newGrid)
    Grid[:] = newGrid[:]
    return Grid

def main():
    Grid = initGrids(64)
    Grid = initCellsAlive(Grid)
    fig, ax = plt.subplots()
    img = ax.imshow(Grid, interpolation='nearest', cmap="gray")
    ani = animation.FuncAnimation(fig, checkNeighbours, fargs=(Grid, img,),
                                  frames = 20,
                                  interval=50)
    plt.show()

if __name__ == "__main__":
    main()