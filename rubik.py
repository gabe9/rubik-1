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

    solve_corner = []

    # Fix corner at top,2,2 (orange, blue)
    wob = findCorner(corner_cube,WHITE,ORANGE,BLUE)
    solve_wob = solveWhiteCornersCorner(wob) + ["Ui"]
    print(solve_wob)

    corner_cube = applySteps(corner_cube,solve_wob)
    solve_corner += solve_wob

    # Fix corner at top,2,0 (blue, red)
    wbr = findCorner(corner_cube,WHITE,BLUE,RED)
    solve_wbr = solveWhiteCornersCorner(wbr) + ["Ui"]
    print(solve_wbr)

    corner_cube = applySteps(corner_cube,solve_wbr)
    solve_corner += solve_wbr

    
    # Fix corner at top,0,0 (red, green)
    wrg = findCorner(corner_cube,WHITE,RED,GREEN)
    solve_wrg = solveWhiteCornersCorner(wrg) + ["Ui"]
    print(solve_wrg)

    corner_cube = applySteps(corner_cube,solve_wrg)
    solve_corner += solve_wrg

    # Fix corner at top,0,2 (green, orange)
    wgo = findCorner(corner_cube,WHITE,GREEN,ORANGE)
    solve_wgo = solveWhiteCornersCorner(wgo) + ["Ui"]
    print(solve_wgo)

    corner_cube = applySteps(corner_cube,solve_wgo)
    solve_corner += solve_wgo

    return solve_corner

# ================

# STEP 3
# ===============

# HELPERS
# ========

def orientBottom(cur, dest):
    if cur == dest:
        return []
    if cur == "front":
        if dest == "left":
            return ["Di"]
        if dest == "right":
            return ["D"]
        if dest == "back":
            return ["D","D"]
    if cur == "left":
        if dest == "front":
            return ["D"]
        if dest == "right":
            return ["D","D"]
        if dest == "back":
            return ["Di"]
    if cur == "right":
        if dest == "front":
            return ["Di"]
        if dest == "back":
            return ["D"]
        if dest == "left":
            return ["D","D"]
    if cur == "back":
        if dest == "front":
            return ["D","D"]
        if dest == "right":
            return ["Di"]
        if dest == "left":
            return ["D"]
    raise Error("Cannot orient " + cur + " to " + dest)

def oppositeSide(side):
    if side == "top":
        return "bot"
    if side == "bot":
        return "top"
    if side == "front":
        return "back"
    if side == "back":
        return "front"
    if side == "right":
        return "left"
    if side == "left":
        return "right"
    return ""

def oppositeBot(side):
    if side == "front":
        return (2,1)
    if side == "right":
        return (1,0)
    if side == "left":
        return (1,2)
    if side == "back":
        return (0,1)


# Middle Edges Moves

# R first = Di, Fi, D, F, D, L, Di, Li
leftToFront = ["Di","Fi","D","F","D","L","Di","Li"]

# B first = D, L, Di, Li, Di, Fi, D, F
frontToLeft = ["D","L","Di","Li","Di","Fi","D","F"]
# BO
# O first = D, F, Di, Fi, Di, Ri, D, R
rightToFront = ["D","F","Di","Fi","Di","Ri","D","R"]

# B first = Di, Ri, D, R, D, F, Di, Fi
frontToRight = ["Di","Ri","D","R","D","F","Di","Fi"]

# Fix back
# GR
# R first = D, B, Di, Bi, Di, Li, D, L
leftToBack = ["D","B","Di","Bi","Di","Li","D","L"]

# G first = Di, Li, D, L, D, B, Di, Bi
backToLeft = ["Di","Li","D","L","D","B","Di","Bi"]

# GO
# O first = Di, Bi, D, B, D, R, Di, Ri
rightToBack = ["Di","Bi","D","B","D","R","Di","Ri"]

# G first = D, R, Di, Ri, Di, Bi, D, B
backToRight = ["D","R","Di","Ri","Di","Bi","D","B"]

def solveMiddleEdge(cur, dest):
    """
    This is used to move the edge from cur to the dest
    @ref frontToLeft, frontToRight, rightToFront, leftToFront
    @ref backToLeft, backToRight, rightToBack, leftToBack
    """

    # First check if already there
    for key in cur:
        for dkey in dest:
            if key == dkey and cur[key] == dest[dkey]:
                return []

    # Check if in middle row somewhere
    for key in cur:
        if key == "bot":
            # the correct block is on the bottom
            break
            
        # we need to move this and try again
        #if (key == "right" or key == "left"):
           # return solveMiddleEdge({ key : (2,1) }, cur) + solveMiddleEdge({ oppositeSide(key) : (2,1) }, dest)
        #if (key == "back" or key == "front"):  
        if cur[key] == (1,0) or cur[key] == (1,2):
            replace = { key : (2,1) }
            return solveMiddleEdge(replace, cur) + solveMiddleEdge({ "bot" : oppositeBot(key) }, dest)

    solved = []
    # Orient bottom correctly
    for key in cur:
        if key == "bot":
            start = "front"
            if cur[key] == (0,1):
                start = "front"
            elif cur[key] == (1,0):
                start = "left"
            elif cur[key] == (1,2):
                start = "right"
            elif cur[key] == (2,1):
                start = "back"

            for dkey in dest:
                if (dkey == "front" and dest[dkey] == (1,0)) or (dkey == "back" and dest[dkey] == (1,2)):
                    solved += orientBottom(start,"left")
                else:
                    solved += orientBottom(start,"right")
        else:
            for dkey in dest:
                solved += orientBottom(key,dkey)

    # apply correct algorithm
    for key in cur:
        for dkey in dest:
            if dkey == "front":
                if dest[dkey] == (1,0):
                    if key == "bot":
                        # left to front
                        solved += leftToFront
                    else:
                        # front to left
                        solved += frontToLeft

                elif dest[dkey] == (1,2):
                    if key == "bot":
                        # right to front
                        solved += rightToFront

                    else:
                        # front to right
                        solved += frontToRight

            if dkey == "back":
                if dest[dkey] == (1,0):
                    if key == "bot":
                        # right to back
                        solved += rightToBack
                    
                    else:
                        # back to right
                        solved += backToRight
                    
                elif dest[dkey] == (1,2):
                    if key == "bot":
                        # left to back
                        solved += leftToBack

                    else:
                        # back to left
                        solved += backToLeft
            if dkey == "left":
                if dest[dkey] == (1,0):
                    if key == "bot":
                        # back to left
                        solved += backToLeft
                    else:
                        # left to back
                        solved += leftToBack
                elif dest[dkey] == (1,2):
                    if key == "bot":
                        # front to left
                        solved += frontToLeft
                    else:
                        # left to front
                        solved += leftToFront
            if dkey == "right":
                if dest[dkey] == (1,0):
                    if key == "bot":
                        solved += frontToRight
                    else:
                        solved += rightToFront
                elif dest[dkey] == (1,2):
                    if key == "bot":
                        solved += backToRight
                    else:
                        solved += rightToBack

    print(solved)

    return solved
# =========

def solveMiddleEdges(cube):
    """
    Used in step 3 to solve the middle edges
    """
    middle_cube = deepcopy(cube)

    solve_middle = []

    # Fix front
    # BR

    edgeBR = findEdge(middle_cube,BLUE,RED)
    solve_BR = solveMiddleEdge(edgeBR, { "front": (1,0) })

    print(solve_BR)
    middle_cube = applySteps(middle_cube,solve_BR)
    solve_middle += solve_BR

    edgeBO = findEdge(middle_cube,BLUE,ORANGE)
    solve_BO = solveMiddleEdge(edgeBO, { "front": (1,2) })

    print(solve_BO)
    middle_cube = applySteps(middle_cube,solve_BO)
    solve_middle += solve_BO

    edgeGR = findEdge(middle_cube,GREEN,RED)
    solve_GR = solveMiddleEdge(edgeGR, { "back" : (1,2) })

    print(solve_GR)
    middle_cube = applySteps(middle_cube, solve_GR)
    solve_middle += solve_GR

    edgeGO = findEdge(middle_cube,GREEN,ORANGE)
    solve_GO = solveMiddleEdge(edgeGO, { "back" : (1,0) })

    print(solve_GO)
    middle_cube = applySteps(middle_cube, solve_GO)
    solve_middle += solve_GO

    return solve_middle

# ===============

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
    print("Step 3: Solve the Middle Edges\n")
    step_three = solveMiddleEdges(solved)
    solved = applySteps(solved, step_three)

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
