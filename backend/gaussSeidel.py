# Gauss Seidel algorithm using golden seaction search as optimization method in specific direction
from sympy import *
from math import *


# p0 is a whole starting point, n is a number of variables in function
from backend.goldenSectionSearch import goldenSectionSearch

XL = -5     # lower bound for golden section search
XU = 5      # upper bound for golden section search
pointList = []  # first element is the initial guess, the rest is coming from algorithm iterations

# Function adds value of given point to the POINT vector
def changePoint(point, argNumber, argValue):
    newPoint = point.copy()
    newPoint[argNumber] = argValue
    return newPoint

# ARGs:
# function - given function by the user for the optimization task
# precision - ??
# L - max number of iterations
# p0 - starting point chosen by the user
# intervalLength
def gaussSeidel(function, givenExpression, precison, L, p0, intervalLength):
    i = 0
    it = 0
    point = p0              # first point is our initial guess
    funcValDiff = 10000
    twoPointDist = 10000
    pointList.append(p0)    # adding initial point (guess) to list of all points
    n = len(point)          # number of entered function variables

    while (i < L and funcValDiff > 0.00000000000000008 and twoPointDist > 0.005):
        for pos in range(n):
            xl = point[pos] - intervalLength
            xu = point[pos] + intervalLength

            f = lambda x: function(givenExpression, changePoint(point, pos, x))
            value = goldenSectionSearch(f, xl, xu)      # value is xopt
            point = changePoint(point, pos, value)

        pointList.append(point)
        i += 1
        it += 1
        sumOfSquares = 0
        # computing one of the stop criterion - difference between 2 function values for specific points
        if len(pointList) >= 2:
            funcValDiff = abs(function(givenExpression, pointList[it]) - function(givenExpression, pointList[it - 1]))

        # computing one of the stop criterion - distance diff between 2 points - euclidean norm
        if len(pointList) >= 2:
            for z in range(n):
                sumOfSquares += (pointList[it][z])**2
            p1 = sqrt(sumOfSquares)
            for z in range(n):
                sumOfSquares += (pointList[it-1][z])**2
            p2 = sqrt(sumOfSquares)
        twoPointDist = abs(p1-p2)

    # printing
    print("Lista punktow")
    print(pointList)
    return pointList
