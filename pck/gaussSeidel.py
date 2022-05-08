# Gauss Seidel algorithm using golden seaction search as optimization method in specific direction
from sympy import *

# p0 is a whole starting point, n is a number of variables in function
from pck.goldenSectionSearch import goldenSectionSearch

XL = -5     # lower bound for golden section search
XU = 5      # upper bound for golden section search

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
    point = p0
    n = len(point)      # number of entered function variables
    while (i < L):
        for pos in range(n):
            xl = point[pos] - intervalLength
            xu = point[pos] + intervalLength

            f = lambda x: function(changePoint(point, pos, x))
            value = goldenSectionSearch(f, xl, xu)
            point = changePoint(point, pos, value)
        i += 1

