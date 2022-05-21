# Golden section search
from sympy import *
from math import *

def goldenSectionSearch(function, xl, xu):
    error = 100; i = 1

    ratio = (5 ** 0.5 - 1) / 2      # golden ratio
    D = ratio * (xu - xl)
    x1 = xl + D
    x2 = xu - D
    f1 = function(x1)               # compting function value in this point
    f2 = function(x2)

    # Golden section search
    while error > 0.1:
        if f1 > f2:
            xl = x2
            x2 = x1
            f2 = f1
            x1 = xl + ratio *(xu - xl)
            f1 = function(x1)
        else:
            xu = x1
            x1 = x2
            f1 = f2
            x2 = xu - ratio * (xu - xl)
            f2 = function(x2)

        if f1 > f2:
            xopt = x1
        else:
            xopt = x2

        error = (1 - ratio) * abs((xu-xl) / xopt) * 100
        i += 1
    return xopt



