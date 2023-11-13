
def isFull():
    for block in grid:
        if block == None:
            return False
    return True

def winHorizontal():
    for i in range(2):
        if(grid[i][0] == grid[i][1] == grid[i][2]):
            return grid[i][0]
    return None
        
def winVertical():
    for i in range(2):
        if(grid[0][i] == grid[1][i] == grid[2][i]):
            return grid[0][i]
    return None

def winDiagonal():
    if((grid[0][0] == grid[1][1] == grid[2][2]) or (grid[2][0] == grid[1][1] == grid[0][2])):
        return grid[1][1]
    return None

def isOver():
    if(winHorizontal() != None or winVertical() != None or winDiagonal() != None or isFull()):
        return True
    else:
        return False

def printGrid():
    for i in range(2):
        for j in range(2):
            row = ""
            if(j != 0):
                row += " |"
            x = grid[i][j]
            if(x == None):
                x = " "
            row += " " + x
        print(row)
        if(i != 2):
            print("---|---|---")


grid = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
while(not isOver()):
    printGrid()
    playerInput = input("Enter next guess: ")