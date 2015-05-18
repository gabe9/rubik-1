from cube import *

# Functions used to solve the cube
def findColorByPosition(cube, color, position, excluded=[]):
    for side in cube:
        if side in excluded:
            continue
        if cube[side][position[0]][position[1]] == color:
            return side

    raise Error("Color " + color + " not found where at position " + str(position))

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

# YELLOW CROSS HELPERS
# ===============

def hasYellowCross(side):
    return side[0][1] == YELLOW and side[1][0] == YELLOW and side[1][2] == YELLOW and side[2][1] == YELLOW

def hasLine(side):
    return (side[0][1] == YELLOW and side[2][1] == YELLOW) or (side[1][0] == YELLOW and side[1][2] == YELLOW)

def hasOne(side):
    return (not hasLine(side)) and (not hasCrooked(side))

def hasCrooked(side):
    return (side[0][1] == YELLOW and (side[1][0] == YELLOW or side[1][2] == YELLOW)) or (side[2][1] == YELLOW and (side[1][0] == YELLOW or side[1][2] == YELLOW))

def orientCrooked(side):
    if (side[0][1] == YELLOW):
        if (side[1][0] == YELLOW):
            return []
        elif (side[1][2] == YELLOW):
            return ["Di"]
    if (side[2][1] == YELLOW):
        if (side[1][0] == YELLOW):
            return ["D"]
        elif (side[1][2] == YELLOW):
            return ["D","D"]
    return []

def orientLine(side):
    if (side[0][1] == YELLOW):
        return ["D"]
    return []


# SOLVE THE YELLOW CROSS
# ===============
def solveYellowCross(cube):
    """
    This solves the yellow cross on the bottom
    while not hasYellowCross:
        1. orient correctly
        2. perform correct algorithm
    """
    cross_cube = deepcopy(cube)

    solved = []
    alg_one = ["F","D","L","Di","Li","Fi"]
    alg_two = ["F","L","D","Li","Di","Fi"]

    while(not hasYellowCross(cross_cube["bot"])):
        if (hasOne(cross_cube["bot"])):
            solved += alg_one
            cross_cube = applySteps(cross_cube,alg_one)
            print(alg_one)
        elif (hasCrooked(cross_cube["bot"])):
            alg_crooked = orientCrooked(cross_cube["bot"]) + alg_one
            solved += alg_crooked
            cross_cube = applySteps(cross_cube,alg_crooked)
            print(alg_crooked)
        elif (hasLine(cross_cube["bot"])):
            alg_line = orientLine(cross_cube["bot"]) + alg_two
            solved += alg_line
            cross_cube = applySteps(cross_cube,alg_line)
            print(alg_line)
    return solved

# ===============

# YELLOW CORNERS HELPERS
# ===============
def numYellowCorners(side):
    num = 0
    if (side[0][0] == YELLOW):
        num += 1
    if (side[0][2] == YELLOW):
        num += 1
    if (side[2][0] == YELLOW):
        num += 1
    if (side[2][2] == YELLOW):
        num += 1

    return num

def hasYellowCorners(side):
    return numYellowCorners(side) == 4

def findYellowCornerSide(bot):
    if (bot[0][0] == YELLOW):
        return "left"
    if (bot[0][2] == YELLOW):
        return "front"
    if (bot[2][0] == YELLOW):
        return "back"
    if (bot[2][2] == YELLOW):
        return "right"
    
    raise Error("No yellow corners on bot")

def orientYellowCorner(cube,side):
    current_side = "front"
    if (side == "bot"):
        # find corner on bot
        current_side = findYellowCornerSide(cube["bot"])
        side = "front"
    elif (side == "right"):
        current_side = findColorByPosition(cube,YELLOW,(2,0),excluded=["top","bot"])
    elif (side == "front"):
        current_side = findColorByPosition(cube,YELLOW,(2,2),excluded=["top","bot"])
    return orientBottom(current_side,side) 

# SOLVE YELLOW CORNERS
# ===============
def solveYellowCorners(cube):
    """
    This function solves the yellow corners
    while not hasYellowCorners:
        Down is Top: R, U, Ri, U, R, U, U, Ri
        No Corners: orient Y on right:(2,0)
        One Corner: orient corner on bot:(2,0)
        Any Two Corners: orient Y on front(2,2)
    """
    corner_cube = deepcopy(cube)

    solved = []
    alg = ["L","D","Li","D","L","D","D","Li"]

    while(not hasYellowCorners(corner_cube["bot"])):
        alg_corners = []
        num_corners = numYellowCorners(corner_cube["bot"])
        if (num_corners == 0):
            # orient Y on right:(2,0)
            alg_corners += orientYellowCorner(corner_cube,"right")
        elif (num_corners == 1):
            # orient Y on bot:(2,0)
            alg_corners += orientYellowCorner(corner_cube,"bot")
        else:
            # orient Y on front(2,2)
            alg_corners += orientYellowCorner(corner_cube,"front")

        alg_corners += alg
        corner_cube = applySteps(corner_cube,alg_corners)
        print(alg_corners)
        solved += alg_corners

    return solved

# ===============

# SWAP CORNERS HELPERS
# ===============
def hasProperCorners(cube):
    for side in cube:
        if (not side == "top") and (not side == "bot"):
            if (not cube[side][2][0] == cube[side][2][2]):
                return False
    return True

def findCorrectCornerSide(cube):
    for side in cube:
        if (not side == "top") and (not side == "bot"):
            if (cube[side][2][0] == cube[side][2][2]):
                return side
    
    return None

# SOLVE SWAP CORNERS
# ===============
def solveSwapCorners(cube):
    """
    This function swaps the corners to place them in the proper position
    Ri,F,Ri,B,B,R,Fi,Ri,B,B,R,R,Ui
    while not hasProperCorners(swap_cube):
        position correct corners in back
        apply alg

    orient bottom correctly
    """
    swap_cube = deepcopy(cube)

    solved = []
    alg = ["Li","F","Li","B","B","L","Fi","Li","B","B","L","L","Di"]

    while (not hasProperCorners(swap_cube)):
        current_alg = []
        
        correct_side = findCorrectCornerSide(swap_cube)
        if (not correct_side == None):
            current_alg += orientBottom(correct_side,"back")
        current_alg += alg
        print(current_alg)

        swap_cube = applySteps(swap_cube,current_alg)
        solved += current_alg

    # might need to orient bottom correctly
    orient = orientBottom(findColorByPosition(swap_cube,BLUE,(2,2),excluded=["top","bot"]),"front")
    solved += orient     
    print(orient)
    return solved

# ===============

# ROTATE EDGES HELPERS
# ===============
def hasCorrectEdges(cube):
    for side in cube:
        if (not side == "top") and (not side == "bot"):
            if (not cube[side][2][0] == cube[side][2][1]):
                return False
    return True

def oppositeColor(color):
    if (color == BLUE):
        return GREEN
    if (color == GREEN):
        return BLUE
    
    if (color == RED):
        return ORANGE
    if (color == ORANGE):
        return RED

    if (color == WHITE):
        return YELLOW
    if (color == YELLOW):
        return WHITE

    raise Error("Invalid Color")

def decideRotation(cube,color):
    edge = findColorByPosition(cube,color,(2,1),excluded=["top","bot"])
    corner = findColorByPosition(cube,color,(2,0),excluded=["top","bot"])

    diff = orientBottom(edge,corner)
    
    if (len(diff) == 0):
        return decideRotation(cube,oppositeColor(color))

    if (len(diff) == 2):
        return True
    if (diff[0] == "D"):
        return True
    if (diff[0] == "Di"):
        return False

    return False

def findProperSide(cube):
    for side in cube:
        if side not in ["top","bot"]:
            row = getRow(cube,side,2)
            if (row[0] == row[1] and row[0] == row[2]):
                return side
    return None

# Solve Rotate Edges
# ===============
def solveRotateEdges(cube):
    """
    This function rotates the bottom edges until they are correct
    Clockwise: F, F, U, L, Ri, F, F, Li, R, U, F, F
    Counter:   F, F, Ui, L, Ri, F, F, Li, R, Ui, F F
    """
    rotate_cube = deepcopy(cube)

    solved = []

    clock_alg = ["F","F","D","R","Li","F","F","Ri","L","D","F","F"]
    counter_alg = ["F","F","Di","R","Li","F","F","Ri","L","Di","F","F"]

    while (not hasCorrectEdges(rotate_cube)):
        # clockwise or counter?
        current_alg = []

        needsClockwise = decideRotation(rotate_cube,BLUE)
        
        # orient proper side to back
        proper_side = findProperSide(rotate_cube)
        if (proper_side):
            current_alg += orientBottom(proper_side,"back")
 
        if (needsClockwise):
            current_alg += clock_alg
        else:
            current_alg += counter_alg

        rotate_cube = applySteps(rotate_cube,current_alg)

        print(current_alg)
        solved += current_alg

    # might need to orient bottom correctly
    orient = orientBottom(findColorByPosition(rotate_cube,BLUE,(2,1),excluded=["top","bot"]),"front")
    solved += orient     
    print(orient)
    return solved

# ===============

def solve(cube):
    """
    This function solves the cube and outputs the moves to do so
    """
    solved = deepcopy(cube)

    # Step 1: White Cross
    print("Step 1: Solve the White Cross\n")
    
    step_one = solveWhiteCross(solved)
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
    print("Step 4: Solve the Yellow Cross\n")
    step_four = solveYellowCross(solved)
    solved = applySteps(solved, step_four)

    # Step 5: Yellow Corners
    print("Step 5: Solve the Yellow Corners\n")
    step_five = solveYellowCorners(solved)
    solved = applySteps(solved, step_five)

    # Step 6: Swap Corners
    print("Step 6: Swap the Corners\n")
    step_six = solveSwapCorners(solved)
    solved = applySteps(solved, step_six)

    # Step 7: Rotate Edges
    print("Step 7: Rotate the Edges\n")
    step_seven = solveRotateEdges(solved)
    solved = applySteps(solved, step_seven)

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
