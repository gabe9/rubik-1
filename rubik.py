from cube import *

# Functions used to solve the cube

def findEdge(cube, primary, secondary):
    """
    This function returns the position and side of the given edge/corner
    This uses the primary color to determine the face
    """
    # Create easy side references
    top = cube["top"]
    front = cube["front"]
    left = cube["left"]
    back = cube["back"]
    right = cube["right"]
    bot = cube["bot"]

    # Top
    if (top[0][1] == primary):
        if (back[0][1] == secondary):
            return { "top" : (0,1) }
    if (top[1][0] == primary):
        if (left[0][1] == secondary):
            return { "top" : (1,0) }
    if (top[1][2] == primary):
        if (right[0][1] == secondary):
            return { "top" : (1,2) }
    if (top[2][1] == primary):
        if (front[0][1] == secondary):
            return { "top" : (2,1) }

    # Front
    if (front[0][1] == primary):
        if (top[2][1] == secondary):
            return { "front" : (0,1) }
    if (front[1][0] == primary):
        if (left[1][2] == secondary):
            return { "front" : (1,0) }
    if (front[1][2] == primary):
        if (right[1][0] == secondary):
            return { "front" : (1,2) }
    if (front[2][1] == primary):
        if (bot[0][1] == secondary):
            return { "front" : (2,1) }

    # Left
    if (left[0][1] == primary):
        if (top[1][0] == secondary):
            return { "left" : (0,1) }
    if (left[1][0] == primary):
        if (back[1][2] == secondary):
            return { "left" : (1,0) }
    if (left[1][2] == primary):
        if (front[1][0] == secondary):
            return { "left" : (1,2) }
    if (left[2][1] == primary):
        if (bot[1][0] == secondary):
            return { "left" : (2,1) }

    # Back
    if (back[0][1] == primary):
        if (top[0][1] == secondary):
            return { "back" : (0,1) }
    if (back[1][0] == primary):
        if (right[1][2] == secondary):
            return { "back" : (1,0) }
    if (back[1][2] == primary):
        if (left[1][0] == secondary):
            return { "back" : (1,2) }
    if (back[2][1] == primary):
        if (bot[2][1] == secondary):
            return { "back" : (2,1) }

    # Right
    if (right[0][1] == primary):
        if (top[1][2] == secondary):
            return { "right" : (0,1) }
    if (right[1][0] == primary):
        if (front[1][2] == secondary):
            return { "right" : (1,0) }
    if (right[1][2] == primary):
        if (back[1][0] == secondary):
            return { "right" : (1,2) }
    if (right[2][1] == primary):

        if (bot[1][2] == secondary):
            return { "right" : (2,1) }

    # Bottom
    if (bot[0][1] == primary):
        if (front[2][1] == secondary):
            return { "bot" : (0,1) }
    if (bot[1][0] == primary):
        if (left[2][1] == secondary):
            return { "bot" : (1,0) }
    if (bot[1][2] == primary):
        if (right[2][1] == secondary):
            return { "bot" : (1,2) }
    if (bot[2][1] == primary):
        if (back[2][1] == secondary):
            return { "bot" : (2,1) }
    
    raise Error("The edge " + primary + " + " + secondary + " was not found!")

def findCorner(cube, primary, secondary, tertiary):
    """
    This function returns the position and side of the given corner
    This uses the primary color to determine the face
    """
    # Create easy side references
    top = cube["top"]
    front = cube["front"]
    left = cube["left"]
    back = cube["back"]
    right = cube["right"]
    bot = cube["bot"]

    # Top
    if (top[0][0] == primary):
        if (left[0][0] == secondary):
            return { "top" : (0,0) }
    if (top[0][2] == primary):
        if (back[0][0] == secondary):
            return { "top" : (0,2) }
    if (top[2][0] == primary):
        if (front[0][0] == secondary):
            return { "top" : (2,0) }
    if (top[2][2] == primary):
        if (right[0][0] == secondary):
            return { "top" : (2,2) }

    # Front
    if (front[0][0] == primary):
        if (left[0][2] == secondary):
            return { "front" : (0,0) }
    if (front[0][2] == primary):
        if (top[2][2] == secondary):
            return { "front" : (0,2) }
    if (front[2][0] == primary):
        if (bot[0][0] == secondary):
            return { "front" : (2,0) }
    if (front[2][2] == primary):
        if (right[2][0] == secondary):
            return { "front" : (2,2) }

    # Left
    if (left[0][0] == primary):
        if (back[0][2] == secondary):
            return { "left" : (0,0) }
    if (left[0][2] == primary):
        if (top[2][0] == secondary):
            return { "left" : (0,2) }
    if (left[2][0] == primary):
        if (bot[2][0] == secondary):
            return { "left" : (2,0) }
    if (left[2][2] == primary):
        if (front[2][0] == secondary):
            return { "left" : (2,2) }

    # Back
    if (back[0][0] == primary):
        if (right[0][2] == secondary):
            return { "back" : (0,0) }
    if (back[0][2] == primary):
        if (top[0][0] == secondary):
            return { "back" : (0,2) }
    if (back[2][0] == primary):
        if (bot[2][2] == secondary):
            return { "back" : (2,0) }
    if (back[2][2] == primary):
        if (left[2][0] == secondary):
            return { "back" : (2,2) }

    # Right
    if (right[0][0] == primary):
        if (front[0][2] == secondary):
            return { "right" : (0,0) }
    if (right[0][2] == primary):
        if (top[0][2] == secondary):
            return { "right" : (0,2) }
    if (right[2][0] == primary):
        if (bot[0][2] == secondary):
            return { "right" : (2,0) }
    if (right[2][2] == primary):
        if (back[2][0] == secondary):
            return { "right" : (2,2) }

    # Bottom
    if (bot[0][0] == primary):
        if (left[2][2] == secondary):
            return { "bot" : (0,0) }
    if (bot[0][2] == primary):
        if (front[2][2] == secondary):
            return { "bot" : (0,2) }
    if (bot[2][0] == primary):
        if (back[2][2] == secondary):
            return { "bot" : (2,0) }
    if (bot[2][2] == primary):
        if (right[2][2] == secondary):
            return { "bot" : (2,2) }
    
    raise Error("The corner " + primary + " + " + secondary + " + " + tertiary + " was not found!")

def applySteps(cube, steps):
    """
    This applies the steps to the given cube
    """
    step_cube = deepcopy(cube)

    for step in steps:
        step_cube = do_step(step_cube,step)

    return step_cube

# White Cross Helpers
# ===================
def solveWhiteCrossBlue(blue):
    """
    This gives the steps to get the WB edge in place
    """
    for key in blue:
        if (key == "front"):
            if (blue[key] == (0,1)):
                return ["Fi"] + solveWhiteCrossBlue({ "front" : (1,0) })
            elif (blue[key] == (2,1)):
                return ["F"] + solveWhiteCrossBlue({ "front" : (1,0) })
            elif (blue[key] == (1,2)):
                return ["F"] + solveWhiteCrossBlue({ "front" : (2,1) })
            elif (blue[key] == (1,0)):
                return ["U","Li","Ui"]
        if (key == "top"):
            if (blue[key] == (0,1)):
                return ["B"] + solveWhiteCrossBlue({ "left" : (1,0) })
            elif (blue[key] == (1,0)):
                return ["L"] + solveWhiteCrossBlue({ "front" : (1,0) })
            elif (blue[key] == (1,2)):
                return ["Ri"] + solveWhiteCrossBlue({ "front" : (1,2) })
            elif (blue[key] == (2,1)):
                return []
        if (key == "left"):
            if (blue[key] == (0,1)):
                return ["L", "F"]
            elif (blue[key] == (1,0)):
                return ["Li","D","L"] + solveWhiteCrossBlue({ "front" : (2,1) })
            elif (blue[key] == (2,1)):
                return ["D"] + solveWhiteCrossBlue({ "front" : (2,1) })
            elif (blue[key] == (1,2)):
                return ["F"]
        if (key == "back"):
            if (blue[key] == (0,1)):
                return ["B","B"] + solveWhiteCrossBlue({ "back" : (2,1) })
            elif (blue[key] == (1,0)):
                return ["Bi","D","B"] + solveWhiteCrossBlue({ "left" : (2,1) })
            elif (blue[key] == (1,2)):
                return ["B","D","Bi"] + solveWhiteCrossBlue({ "left" : (2,1) })
            elif (blue[key] == (2,1)):
                return ["D"] + solveWhiteCrossBlue({ "left" : (2,1) })
        if (key == "right"):
            if (blue[key] == (0,1)):
                return ["Ri","Fi"]
            elif (blue[key] == (1,0)):
                return ["Fi"]
            elif (blue[key] == (1,2)):
                return ["R","Di","Ri"] + solveWhiteCrossBlue({ "front" : (2,1) })
            elif (blue[key] == (2,1)):
                return ["Di"] + solveWhiteCrossBlue({ "front" : (2,1) })
        if (key == "bot"):
            if (blue[key] == (0,1)):
                return ["F","F"]
            elif (blue[key] == (1,0)):
                return ["D"] + solveWhiteCrossBlue({ "bot" : (0,1) })
            elif (blue[key] == (1,2)):
                return ["Di"] + solveWhiteCrossBlue({ "bot" : (0,1) })
            elif (blue[key] == (2,1)):
                return ["D", "D"] + solveWhiteCrossBlue({ "bot" : (0,1) })

    return []

def hasWhiteCross(cube):
    """
    This function returns true if the cube has a white cross, else false
    """
    top = cube["top"]
    top_check = (top[0][1] == WHITE) and (top[1][0] == WHITE) and (top[1][2] == WHITE) and (top[2][1] == WHITE)
    
    back = cube["back"]
    back_check = (back[0][1] == GREEN)

    left = cube["left"]
    left_check = (left[0][1] == RED)

    right = cube["right"]
    right_check = (right[0][1] == ORANGE)

    front = cube["front"]
    front_check = (front[0][1] == BLUE)

    return top_check and front_check and left_check and right_check and back_check
# ===================

def solveWhiteCross(cube):
    """
    This function solves the white cross and returns the moves to do so
    """
    cross_cube = deepcopy(cube)
    solve_cross = []

    # Blue
    blue = findEdge(cross_cube,WHITE,BLUE)
    solve_blue = solveWhiteCrossBlue(blue) + ["Ui"]
    print(solve_blue)
    
    cross_cube = applySteps(cross_cube,solve_blue)
    solve_cross += solve_blue
    
    # Red
    red = findEdge(cross_cube,WHITE,RED)
    solve_red = solveWhiteCrossBlue(red) + ["Ui"]
    print(solve_red)

    cross_cube = applySteps(cross_cube,solve_red)
    solve_cross += solve_red
   
    # Green
    green = findEdge(cross_cube,WHITE,GREEN)
    solve_green = solveWhiteCrossBlue(green) + ["Ui"]
    print(solve_green)

    cross_cube = applySteps(cross_cube,solve_green)
    solve_cross += solve_green

    # Orange
    orange = findEdge(cross_cube,WHITE,ORANGE)
    solve_orange = solveWhiteCrossBlue(orange) + ["Ui"]
    print(solve_orange)

    cross_cube = applySteps(cross_cube,solve_orange)
    solve_cross += solve_orange
    
    return solve_cross

    
# ================


# White Corners Helper Functions
# ================
def solveWhiteCornersCorner(corner):
    
    for key in corner:
        if (key == "front"):
            if (corner[key] == (0,0)):
                return ["L","Di","Li"] + solveWhiteCornersCorner({ "front" : (2,0) })
            elif (corner[key] == (0,2)):
                return ["Ri","D","R"] + solveWhiteCornersCorner({ "front" : (2,2) })
            elif (corner[key] == (2,0)):
                return ["D","Ri","Di","R"]
            elif (corner[key] == (2,2)):

                return ["F","D","Fi"]

        elif (key == "top"):
            if (corner[key] == (0,0)):
                return ["B","D","Bi"] + solveWhiteCornersCorner({ "front" : (2,0) })
            elif (corner[key] == (0,2)):
                return ["Bi","Di","B"] + solveWhiteCornersCorner({ "front" : (2,2) })
            elif (corner[key] == (2,0)):
                return ["L"] + solveWhiteCornersCorner({ "front" : (2,0) }) + ["Li"]
            elif (corner[key] == (2,2)):
                return []

        elif (key == "left"):
            if (corner[key] == (0,0)):
                return ["Li","D"] + solveWhiteCornersCorner({ "front" : (2,0) }) + ["L"]
            elif (corner[key] == (0,2)):
                return ["L","D"] + solveWhiteCornersCorner({ "front" : (2,2) }) + ["Li"]
            elif (corner[key] == (2,0)):
                return ["D"] + solveWhiteCornersCorner({ "front": (2,0) })
            elif (corner[key] == (2,2)):
                return ["D"] + solveWhiteCornersCorner({ "front": (2,2) })

        elif (key == "back"):
            if (corner[key] == (0,0)):
                return ["Bi","Di","B"] + solveWhiteCornersCorner({ "right" : (2,0) })
            elif (corner[key] == (0,2)):
                return ["B","D","Bi"] + solveWhiteCornersCorner({ "left" : (2,2) })
            elif (corner[key] == (2,0)):
                return ["Di"] + solveWhiteCornersCorner({ "right" : (2,0) })
            elif (corner[key] == (2,2)):
                return ["Di"] + solveWhiteCornersCorner({ "right" : (2,2) })

        elif (key == "right"):
            if (corner[key] == (0,0)):
                return ["Ri","Di","R"] + solveWhiteCornersCorner({ "front" : (2,0) })
            elif (corner[key] == (0,2)):
                return ["R","Di","Di","Ri","D"] + solveWhiteCornersCorner({ "front" : (2,2) })
            elif (corner[key] == (2,0)):
                return ["Ri","Di","R"]
            elif (corner[key] == (2,2)):
                return ["Di"] + solveWhiteCornersCorner({ "front" : (2,2) })

        elif (key == "bot"):
            if (corner[key] == (0,0)):
                return ["D"] + solveWhiteCornersCorner({ "bot" : (0,2) })
            elif (corner[key] == (0,2)):
                return ["F","Di","Fi"] + solveWhiteCornersCorner({ "back" : (2,2) })
            elif (corner[key] == (2,0)):
                return ["Di"] + solveWhiteCornersCorner({ "bot" : (2,2) })
            elif (corner[key] == (2,2)):
                return ["F","D","D","Fi"] + solveWhiteCornersCorner({ "right" : (2,0) })
    return []

# ================


# STEP 2
# ================
def solveWhiteCorners(cube):
    """
    This function returns the moves to fix the white corners
    """
    corner_cube = deepcopy(cube)
    printCube(corner_cube) 

    solve_corner = []

    # Fix corner at top,2,2 (orange, blue)
    wob = findCorner(corner_cube,WHITE,ORANGE,BLUE)
    print(wob)
    solve_wob = solveWhiteCornersCorner(wob) + ["Ui"]
    print(solve_wob)

    corner_cube = applySteps(corner_cube,solve_wob)
    solve_corner += solve_wob
    printCube(corner_cube) 

    # Fix corner at top,2,0 (blue, red)
    wbr = findCorner(corner_cube,WHITE,BLUE,RED)
    print(wbr)
    solve_wbr = solveWhiteCornersCorner(wbr) + ["Ui"]
    print(solve_wbr)

    corner_cube = applySteps(corner_cube,solve_wbr)
    solve_corner += solve_wbr
    printCube(corner_cube) 

    
    # Fix corner at top,0,0 (red, green)
    wrg = findCorner(corner_cube,WHITE,RED,GREEN)
    print(wrg)
    solve_wrg = solveWhiteCornersCorner(wrg) + ["Ui"]
    print(solve_wrg)

    corner_cube = applySteps(corner_cube,solve_wrg)
    solve_corner += solve_wrg
    printCube(corner_cube) 

    # Fix corner at top,0,2 (green, orange)
    wgo = findCorner(corner_cube,WHITE,GREEN,ORANGE)
    print(wgo)
    solve_wgo = solveWhiteCornersCorner(wgo) + ["Ui"]
    print(solve_wgo)

    corner_cube = applySteps(corner_cube,solve_wgo)
    solve_corner += solve_wgo
    printCube(corner_cube) 

    return solve_corner

def solve(cube):
    """
    This function solves the cube and outputs the moves to do so
    """
    solved = deepcopy(cube)

    # Step 1: White Cross
    print("Step 1: Solve the White Cross\n")
    
    step_one = solveWhiteCross(solved)
    print(step_one)
    solved = applySteps(solved, step_one)
    if (not hasWhiteCross(solved)):
        raise Error("White Cross not solved")

    # Step 2: White Corners
    print("Step 2: Solve the White Corners\n")

    step_two = solveWhiteCorners(solved)
    solved = applySteps(solved, step_two)

    # Step 3: Middle Edges
    #step_three = solveMiddleEdges(solved)
    #solved = applySteps(solved, step_three)

    # Step 4: Yellow Cross
    #step_four = solveYellowCross(solved)
    #solved = applySteps(solved, step_four)

    # Step 5: Yellow Corners
    #step_five = solveYellowCorners(solved)
    #solved = applySteps(solved, step_five)

    # Step 6: Swap Corners
    #step_six = solveSwapCorners(solved)
    #solved = applySteps(solved, step_six)

    # Step 7: Rotate Edges
    #step_seven = solveRotateEdges(solved)
    #solved = applySteps(solved, step_seven)

    return solved

# ===============
# Main function

def main() :
    testCube = makeCube(3)
    printCube(testCube)
    
    r = input()
    while(r):
        if (r == "exit" or r == "q"):
            exit()
            break
        elif(r == "rand"):
            testCube = randomizeCube(testCube,3)
        elif(r == "create"):
            testCube = cubeCreator()
        elif(r == "solve"):
            testCube = solve(testCube)
        else:
            testCube=do_step(testCube,r)


        printCube(testCube)
        r = input()

if __name__ == "__main__" :
    main()
