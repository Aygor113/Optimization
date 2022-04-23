# Golden section search
from sympy import *
def goldenSectionSearch(function, xl, xu):
    #f = lambda x: 4 - x1 ** 2 - 0.2 * x2 ** 3      # First function to verify results
    #f = lambda x: 3*x**3 + 5 * x ** 2 - 7          # Second function to verify results


    # Returns function evaluation
    #def f(function, x):
    #    return (lambda x: function)


    # Initial guess

    #xl = -5; xu = 0

    ##################
    print('iter \t\t\t error \t\t\t xopt')
    error = 100; i = 1

    ratio = (5 ** 0.5 - 1) / 2
    D = ratio * (xu - xl)
    x1 = xl + D
    x2 = xu - D
    f1 = function(x1)
    f2 = function(x2)

    # Golden section search
    while error > 0.1:
        if f1> f2:
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
        #print('%f \t %f \t %f'% (i, error, xopt))
        print(i, error, xopt)
        i += 1
    return xopt



