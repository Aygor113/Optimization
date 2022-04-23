# Gauss Seidel algorithm using golden seaction search as optimization method in specific direction
from sympy import *

# p0 is a whole starting point, n is a number of variables in function
from pck.goldenSectionSearch import goldenSectionSearch

XL = -5
XU = 5

def changePoint(point, argNumber, argValue):
    newPoint = point.copy()
    newPoint[argNumber] = argValue
    return newPoint


def gaussSeidel(function, precison, L, p0):
    i = 0
    # e = []  # direction vector
    point = p0
    n = len(point)      # number of entered function variables

    while (i < L):
        for pos in range(n):
            f = lambda x: function(changePoint(point, pos, x))
            value = goldenSectionSearch(f, XL, XU)
            point = changePoint(point, pos, value)
        i += 1

