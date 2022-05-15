# Main project file
import math

from pck.gaussSeidel import gaussSeidel
from pck.goldenSectionSearch import goldenSectionSearch
INTERVAL_LENGTH = 10

class OptimizationAlgorithm:
    def __init__(self, expression, L, initialPoint, intervalLength):
        self.givenExpression = expression
        self.L = L
        self.p_example = initialPoint
        self.intervalLength = intervalLength

    # function that return mathematical evaluation of given string
    def functionExample(expression, point):
        X = point[0]
        Y = point[1]
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

    def runAlgorithm(self):
        #p_example = [4.5, -1]
        precision = 0.01
        #L = 5

        # ARGs:
        # functionExample - function that returns evaluated expression from string input
        # givenExpression - mathematical expression entered by user, string
        # precision - stop criteria
        # L - max number of iterations
        # p_example - starting point chosen by the user
        # intervalLength -
        pointList = gaussSeidel(OptimizationAlgorithm.functionExample, self.givenExpression, precision, int(self.L), self.p_example, int(self.intervalLength))
        return pointList


    # ZMIENIC WYPISYWANIE W GOLDEN SECTION, NIECH WYPISUJE W GAUSIE PUNKTY w zaleznosci do iteracji
    # dopisać pozostałe warunki stopu
    # zastanowic sie nad przedziałem ??? ( da sie go automatycznie przesuwać)? spytac
    # DLA WIEKSZEJ ILOSCI WYMIARÓW ?? spytac // no tak ma byc
    # poczatek przedzialu to wartosc punktu poczatkowego, a koniec przedzialu podawany jako parametr
    # wykres z poziomicami
