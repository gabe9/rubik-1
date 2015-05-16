
from copy import deepcopy
from random import randint

WHITE = 'W'  #0
BLUE = 'B'   #1
RED = 'R'    #2
GREEN = 'G'  #3
ORANGE = 'O' #4
YELLOW = 'Y' #5

def makeFace(size, color):
    return [[color for x in range(size)] for x in range(size)]


def makeCube(size):
    white = makeFace(size, WHITE)
    blue = makeFace(size, BLUE)
    red = makeFace(size, RED)
    green = makeFace(size, GREEN)
    orange = makeFace(size, ORANGE)
    yellow = makeFace(size, YELLOW)

    return {
            "top" : white,
            "front" : blue,
            "left" : red,
            "back" : green,
            "right" : orange,
            "bot" : yellow  }

def getRow(cube, side, row_num):
    return cube[side][row_num]

def setRow(cube, side, row_num, new_row):
    for i in range(len(new_row)):
        cube[side][row_num][i] = new_row[i]

def getCol(cube, side, col_num):
    return [cube[side][i][col_num] for i in range(len(cube[side]))]

def setCol(cube, side, col_num, new_col):
    for i in range(len(new_col)):
        cube[side][i][col_num] = new_col[i]

# Rotational stuff
def transpose(matrix):
    return [list(i) for i in zip(*matrix)]

def reverseRows(matrix):
    ret = [[0 for x in range(len(matrix))] for x in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            ret[row][len(matrix)-col-1] = matrix[row][col]
    
    return ret

def reverseCols(matrix):
    ret = [[0 for x in range(len(matrix))] for x in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            ret[len(matrix)-row-1][col] = matrix[row][col]
    
    return ret

def rotateFace(face, inverse):
    if (inverse):
        return reverseCols(transpose(face))
    return reverseRows(transpose(face))

def rotateEdges(cube, side, inverse):
    n = len(cube[side])
    temp_cube = deepcopy(cube)

    if (side == "top"):
        oldRow = deepcopy(getRow(temp_cube, "back", 0))
        if (not inverse):
            setRow(temp_cube, "back", 0, getRow(temp_cube, "left", 0))
            setRow(temp_cube, "left", 0, getRow(temp_cube, "front", 0))
            setRow(temp_cube, "front", 0, getRow(temp_cube, "right", 0))
            setRow(temp_cube, "right", 0, oldRow)
        else:
            setRow(temp_cube, "back", 0, getRow(temp_cube, "right", 0))
            setRow(temp_cube, "right", 0, getRow(temp_cube, "front", 0))
            setRow(temp_cube, "front", 0, getRow(temp_cube, "left", 0))
            setRow(temp_cube, "left", 0, oldRow)

    if (side == "bot"):
        oldRow = deepcopy(getRow(temp_cube, "back", n-1))
        if (not inverse):
            setRow(temp_cube, "back", n-1, getRow(temp_cube, "right", n-1))
            setRow(temp_cube, "right", n-1, getRow(temp_cube, "front", n-1))
            setRow(temp_cube, "front", n-1, getRow(temp_cube, "left", n-1))
            setRow(temp_cube, "left", n-1, oldRow)
        else:
            setRow(temp_cube, "back", n-1, getRow(temp_cube, "left", n-1))
            setRow(temp_cube, "left", n-1, getRow(temp_cube, "front", n-1))
            setRow(temp_cube, "front", n-1, getRow(temp_cube, "right", n-1))
            setRow(temp_cube, "right", n-1, oldRow)

    if (side == "front"):
        oldRow = deepcopy(getRow(temp_cube, "top", n-1))
        if (not inverse):
            setRow(temp_cube, "top", n-1, getCol(temp_cube, "left", n-1)[::-1])
            setCol(temp_cube, "left", n-1, getRow(temp_cube, "bot", 0))
            setRow(temp_cube, "bot", 0, getCol(temp_cube, "right", 0)[::-1])
            setCol(temp_cube, "right", 0, oldRow)
        else:
            setRow(temp_cube, "top", n-1, getCol(temp_cube, "right", 0))
            setCol(temp_cube, "right", 0, getRow(temp_cube, "bot", 0)[::-1])
            setRow(temp_cube, "bot", 0, getCol(temp_cube, "left", n-1))
            setCol(temp_cube, "left", n-1, oldRow[::-1])

    if (side == "back"):
        oldRow = deepcopy(getRow(temp_cube, "top", 0))
        if (not inverse):
            setRow(temp_cube, "top", 0, getCol(temp_cube, "right", n-1))
            setCol(temp_cube, "right", n-1, getRow(temp_cube, "bot", n-1)[::-1])
            setRow(temp_cube, "bot", n-1, getCol(temp_cube, "left", 0))
            setCol(temp_cube, "left", 0, oldRow[::-1])
        else:
            setRow(temp_cube, "top", 0, getCol(temp_cube, "left", 0)[::-1])
            setCol(temp_cube, "left", 0, getRow(temp_cube, "bot", n-1))
            setRow(temp_cube, "bot", n-1, getCol(temp_cube, "right", n-1)[::-1])
            setCol(temp_cube, "right", n-1, oldRow)

    if (side == "left"):
        oldCol = deepcopy(getCol(temp_cube, "top", 0))
        if (not inverse):
            setCol(temp_cube, "top", 0, getCol(temp_cube, "back", n-1)[::-1])
            setCol(temp_cube, "back", n-1, getCol(temp_cube, "bot", 0)[::-1])
            setCol(temp_cube, "bot", 0, getCol(temp_cube, "front", 0))
            setCol(temp_cube, "front", 0, oldCol)
        else:
            setCol(temp_cube, "top", 0, getCol(temp_cube, "front", 0))
            setCol(temp_cube, "front", 0, getCol(temp_cube, "bot", 0))
            setCol(temp_cube, "bot", 0, getCol(temp_cube, "back", n-1)[::-1])
            setCol(temp_cube, "back", n-1, oldCol[::-1])

    if (side == "right"):
        oldCol = deepcopy(getCol(temp_cube, "top", n-1))
        if (not inverse):
            setCol(temp_cube, "top", n-1, getCol(temp_cube, "front", n-1))
            setCol(temp_cube, "front", n-1, getCol(temp_cube, "bot", n-1))
            setCol(temp_cube, "bot", n-1, getCol(temp_cube, "back", 0)[::-1])
            setCol(temp_cube, "back", 0, oldCol[::-1])
        else:
            setCol(temp_cube, "top", n-1, getCol(temp_cube, "back", 0)[::-1])
            setCol(temp_cube, "back", 0, getCol(temp_cube, "bot", n-1)[::-1])
            setCol(temp_cube, "bot", n-1, getCol(temp_cube, "front", n-1))
            setCol(temp_cube, "front", n-1, oldCol)

    return temp_cube

def rotate(cube, side, inverse):
    face = rotateFace(cube[side], inverse)
    temp_cube = rotateEdges(cube, side, inverse)
    temp_cube[side] = face
    return temp_cube

def do_step(cube, move):
    if (move == "F"):
        return rotate(cube,"front",False)
    elif (move == "Fi"):
        return rotate(cube,"front",True)
    elif (move == "U"):
        return rotate(cube,"top",False)
    elif (move == "Ui"):
        return rotate(cube,"top",True)
    elif (move == "L"):
        return rotate(cube,"left",False)
    elif (move == "Li"):
        return rotate(cube,"left",True)
    elif (move == "B"):
        return rotate(cube,"back",False)
    elif (move == "Bi"):
        return rotate(cube,"back",True)
    elif (move == "R"):
        return rotate(cube,"right",False)
    elif (move == "Ri"):
        return rotate(cube,"right",True)
    elif (move == "D"):
        return rotate(cube,"bot",False)
    elif (move == "Di"):
        return rotate(cube,"bot",True)

    raise Error("Invalid move: " + move)


def randomizeCube(cube, level=1): 
    iterations = 9 ** level
    temp_cube = deepcopy(cube)
    for i in range(iterations):
        temp_cube = rotate(temp_cube,list(cube.keys())[randint(0,5)],randint(0,1))

    return temp_cube


def printCube(cube):
    print(" --------------", cube["top"][0],"-------------- ")
    print(" --------------", cube["top"][1],"-------------- ")
    print(" --------------", cube["top"][2],"--------------    R    T    L")
    print(cube["left"][0],cube["front"][0],cube["right"][0],cube["back"][0])
    print(cube["left"][1],cube["front"][1],cube["right"][1],cube["back"][1])
    print(cube["left"][2],cube["front"][2],cube["right"][2],cube["back"][2])
    print(" --------------", cube["bot"][0],"-------------- ")
    print(" --------------", cube["bot"][1],"-------------- ")
    print(" --------------", cube["bot"][2],"-------------- ")

def cubeCreator():
    cube = makeCube(3)

    print("Cube Creator 1.0\n\n")

    for f in cube:
        print("Current Side:", f)
        row1 = input("First Row: ")
        row2 = input("Second Row: ")
        row3 = input("Third Row: ")
        print("\n")
        cube[f] = [list(row1), list(row2), list(row3)]
        print(cube[f])
        print("\n")

    return cube
