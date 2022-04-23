# Main project file
from pck.gaussSeidel import gaussSeidel
from pck.goldenSectionSearch import goldenSectionSearch

variableVector = []

function = input("Please enter a function:\t")
print(function)
"""
x0 = input("Please enter a x0:\t")
print(x0)
precision = input("Please enter precision value:\t")
print(precision)
L = input("Please enter number of iterations:\t")
print(L)
"""

def functionExample(point):
    x = point[0]
    y = point[1]
    return -((x-3)**2 + (y-4)**2 + x*y)

p_example = [-4, -2]
precision = 0.01
L = 5

#print("XOPT: ", goldenSectionSearch(function, -5, 0))
gaussSeidel(functionExample, precision, L, p_example)



# ZMIENIC WYPISYWANIE W GOLDEN SECTION, NIECH WYPISUJE W GAUSIE PUNKTY w zaleznosci do iteracji
# dopisać pozostałe warunki stopu
# zastanowic sie nad przedziałem ??? ( da sie go automatycznie przesuwać)? spytac
# DLA WIEKSZEJ ILOSCI WYMIARÓW ?? spytac
# wykres z poziomicami