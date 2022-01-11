data = [
    [(1, 2), (7, 8), (1, 8), (7, 2), (0, 0), (-2, -5)],
    [(0, 0), (0, 4), (4, 0), (4, 4), (0, -4), (-4, 0), (-4, -4), (1, 2), (5, 0), (0, 5), (5, 5), (10, 11)],
    [(0, 0), (1, 1), (0, 1), (1, 0), (2, 2), (1, 2), (2, 1), (3, 3), (2, 3), (3, 2), (3, 0), (0, 3)],
]
pointsSet = data[0]


def upRightDiagonal(point):
    diagonal = ()
    found = False
    distance = 0
    for i in range(len(pointsSet)):
        xDifference = pointsSet[i][0] - point[0]
        yDifference = pointsSet[i][1] - point[1]
        if xDifference == yDifference > 0:
            if not found:
                diagonal = pointsSet[i]
                found = True
                distance = xDifference
            else:
                if xDifference < distance:
                    diagonal = pointsSet[i]
                    distance = xDifference
    return diagonal


def checkCorners(downLeftCorner, upRightCorner):
    downRightExists = False
    upLeftExists = False
    for index in range(len(pointsSet)):
        if pointsSet[index][0] == downLeftCorner[0] and pointsSet[index][1] == upRightCorner[1]:
            upLeftExists = True
        elif pointsSet[index][0] == upRightCorner[0] and pointsSet[index][1] == downLeftCorner[1]:
            downRightExists = True
    if downRightExists and upLeftExists:
        print("Found a square with down left corer in", downLeftCorner,
              "and up right corner in", upRightCorner, "which", end='')
        return True
    else:
        return False


def isEmpty(downLeftCorner, upRightCorner):
    for i in range(len(pointsSet)):
        isBetweenByX = downLeftCorner[0] <= pointsSet[i][0] <= upRightCorner[0]
        isBetweenByY = downLeftCorner[1] <= pointsSet[i][1] <= upRightCorner[1]
        isDownLeftCorner = pointsSet[i][0] == downLeftCorner[0] and pointsSet[i][1] == downLeftCorner[1]
        isDownRightCorner = pointsSet[i][0] == upRightCorner[0] and pointsSet[i][1] == downLeftCorner[1]
        isUpLeftCorner = pointsSet[i][0] == downLeftCorner[0] and pointsSet[i][1] == upRightCorner[1]
        isUpRightCorner = pointsSet[i][0] == upRightCorner[0] and pointsSet[i][1] == upRightCorner[1]
        isCorner = isDownLeftCorner or isDownRightCorner or isUpLeftCorner or isUpRightCorner
        if isBetweenByX and isBetweenByY and not isCorner:
            return False
    return True


def findSquare(startPoint):
    diagonal = upRightDiagonal(startPoint)
    if len(diagonal) == 0:
        return False
    else:
        if checkCorners(startPoint, diagonal):
            if isEmpty(startPoint, diagonal):
                print(" is empty!")
                return True
            else:
                print(" isn't empty...")
    return False


print(pointsSet)
for i in range(len(pointsSet)):
    findSquare(pointsSet[i])




