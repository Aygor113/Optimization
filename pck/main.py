# Main project file
import math

from pck.gaussSeidel import gaussSeidel
from pck.goldenSectionSearch import goldenSectionSearch
INTERVAL_LENGTH = 10
variableVector = []

givenExpression = input("Please enter a function:\t")
#print(functionExample)

"""
x0 = input("Please enter a x0:\t")
print(x0)
precision = input("Please enter precision value:\t")
print(precision)
L = input("Please enter number of iterations:\t")
print(L)
"""
intervalLength = int(input("Please enter length of the interval: "))
print(intervalLength)

# TEST
#givenExpression = "-((x+2)**2 + (y-1)**2)"

def functionExample(expression, point):
    x = point[0]
    y = point[1]
    if(len(point) == 3):
        z = point[2]
    if(len(point) == 4):
        v = point[3]
    if(len(point) == 5):
        w = point[4]
    return eval(expression)      # funkcja testowa
    #return 1.5 * x - 2.5*y - 1 - math.sin(x+y) - (x-y)**2       # funkcja testowa expected
    #return 0 - (x-4)**2 - (x -y**2)**2       # funkcja testowa
    #return -((x+2)**2 + (y-1)**2)
    #return math.sqrt(16 - x**2 - y**2)
    #return -1*(2*x**2 - 1.05*x**4 + (1/6)*x**6+x*y+y**2)        # funkcja testowa


"""

def functionExample(point):
    x = point[0]
    y = point[1]
    return -1*(2*x**2 - 1.05*x**4 + (1/6)*x**6+x*y+y**2)        # funkcja testowa
    
    #return 1.5 * x - 2.5*y - 1 - math.sin(x+y) - (x-y)**2       # funkcja testowa 2
    #return 0 - (x-4)**2 - (x -y**2)**2       # funkcja testowa 3
    #return -((x+2)**2 + (y-1)**2)
    #return math.sqrt(16 - x**2 - y**2)
"""

p_example = [4.5, -1]
precision = 0.01
L = 5
print("Given expr: " + givenExpression)
# first argument is a function(method)
gaussSeidel(functionExample, givenExpression, precision, L, p_example, intervalLength)



# ZMIENIC WYPISYWANIE W GOLDEN SECTION, NIECH WYPISUJE W GAUSIE PUNKTY w zaleznosci do iteracji
# dopisać pozostałe warunki stopu
# zastanowic sie nad przedziałem ??? ( da sie go automatycznie przesuwać)? spytac
# DLA WIEKSZEJ ILOSCI WYMIARÓW ?? spytac // no tak ma byc
# poczatek przedzialu to wartosc punktu poczatkowego, a koniec przedzialu podawany jako parametr
# wykres z poziomicami