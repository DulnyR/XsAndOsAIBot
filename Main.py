
import copy

grid = [[None for _ in range(3)] for _ in range(3)]
HUMAN = 0
AI = 1
        
def isFull():
    for row in grid:
        for block in row:
            if block == None:
                return False
    return True

def winHorizontal():
    for i in range(3):
        if(grid[i][0] == grid[i][1] == grid[i][2]):
            return grid[i][0]
    return None
        
def winVertical():
    for i in range(3):
        if(grid[0][i] == grid[1][i] == grid[2][i]):
            return grid[0][i]
    return None

def winDiagonal():
    if((grid[0][0] == grid[1][1] == grid[2][2]) or (grid[2][0] == grid[1][1] == grid[0][2])):
        return grid[1][1]
    return None

def isOver():
    if(winHorizontal() == 'X' or winVertical() == 'X' or winDiagonal() == 'X'):
        return -1
    if(winHorizontal() == 'O' or winVertical() == 'O' or winDiagonal() == 'O'):
        return 1
    if(isFull()):
        return 0
    else:
        return False

def printGrid():
    print("  0   1   2")
    for i in range(3):
        if(i == 0): row = "A"
        elif(i == 1): row = "B"
        elif(i == 2): row = "C"
        for j in range(3):
            if(j != 0):
                row += " |"
            square = grid[i][j]
            if(square == None):
                square = " "
            row += " " + square
        print(row)
        if(i != 2):
            print(" ---|---|---")

def getActions():
    actions = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == None:
                actions.append([i, j]);
    return actions

def result(action, player):
    character = 'X'
    if(player == AI): character = 'O'
    grid[action[0]][action[1]] = character

def setSquare(playerInput, player):
    character = 'X'
    if(player == AI):
        character = 'O'
    print("\n" + character + "'s guess\n")
    column = int(playerInput[1])
    if(playerInput[0] == 'A' or playerInput[0] == 0):
        grid[0][column] = character     
    elif(playerInput[0] == 'B' or playerInput[0] == 1):
        grid[1][column] = character
    elif(playerInput[0] == 'C' or playerInput[0] == 2):
        grid[2][column] = character

def getPlayer():
    human = 0
    ai = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'X':
                human += 1
            if grid[i][j] == 'O':
                ai += 1
    if(ai >= human): return HUMAN
    else: return AI

def miniMax(actions):
    global grid
    state = isOver()
    if state is not False:
        return state
    if (getPlayer() == AI):
        value = -2
        copyGrid = copy.deepcopy(grid)
        for action in actions:
            grid = copy.deepcopy(copyGrid)
            result(action, AI)
            newVal = miniMax(getActions())
            value = max(value, newVal)
        grid = copy.deepcopy(copyGrid)
        return value
    else:
        value = 2
        copyGrid = copy.deepcopy(grid)
        for action in actions:
            grid = copy.deepcopy(copyGrid)
            result(action, HUMAN)
            newVal = miniMax(getActions())
            value = min(value, newVal)
        grid = copy.deepcopy(copyGrid)
        return value

def main():
    winner = isOver()
    printGrid()
    while winner is False:
        playerInput = input("\nEnter next guess (e.g. B2): ")
        setSquare(playerInput, HUMAN)
        printGrid()
        actions = getActions()
        bestValue = -2
        for action in actions:
            twoDAction = [action]
            value = miniMax(twoDAction)
            if(value > bestValue):
                bestAction = action
                bestValue = value
        setSquare(bestAction, AI)
        printGrid()
        winner = isOver()
    if(winner == -1): print("\nX WINS!")
    elif(winner == 1): print("\nO WINS!")
    elif(winner == 0): print("\nDRAW!")

main()