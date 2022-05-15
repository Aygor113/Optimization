# Gauss Seidel algorithm using golden seaction search as optimization method in specific direction
from sympy import *

# p0 is a whole starting point, n is a number of variables in function
from pck.goldenSectionSearch import goldenSectionSearch

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
def gaussSeidel(function, precison, L, p0, intervalLength):
    i = 0
    it = 0
    point = p0
    funcValDiff = 10000
    twoPointDist = 10000
    pointList.append(p0)
    n = len(point)      # number of entered function variables
    """or funcValDiff > 0.001"""            # zmiana znaku !!!!!!
    """ i < L"""
    while (i < L and funcValDiff > 0.00000000000000008 and twoPointDist > 0.005):
        for pos in range(n):
            xl = point[pos] - intervalLength
            xu = point[pos] + intervalLength

            f = lambda x: function(changePoint(point, pos, x))
            value = goldenSectionSearch(f, xl, xu)
            point = changePoint(point, pos, value)

        prevPoint = point
        pointList.append(point)
        i += 1
        it += 1
        sumOfSquares = 0
        # computing one of the stop criterion - difference between 2 function values for specific points
        if len(pointList) >= 2:
            funcValDiff = abs(function(pointList[it]) - function(pointList[it - 1]))
        print("WARTOŚ FUNKCJI: " + str(funcValDiff))

        # computing one of the stop criterion - distance diff between 2 points - euclidean norm
        if len(pointList) >=2:
            for z in range(n):
                sumOfSquares += (pointList[it][z])**2
            p1 = sumOfSquares
            for z in range(n):
                sumOfSquares += (pointList[it-1][z])**2
            p2 = sumOfSquares
        twoPointDist = abs(p1-p2)

    # printing
    print("Lista punktow")
    print(pointList)
