import tkinter
from cgitb import reset
from tkinter import *
import matplotlib.pyplot as plt
import numpy
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from backend import main

#General
from tkinter import messagebox

from backend.main import OptimizationAlgorithm

root = Tk()
root.title('Gauss - Seidl Algorithm')
root.geometry("1000x600")
root.resizable(True,True)

frame_radioButtons = tkinter.Frame(root)
frame_radioButtons.place(x=300, y=300)

#Labels

Label(root, text="Gauss - Seidl Algorithm",font=("Helvetica", 18)).place(x=350, y=25)           #Title label
Label(root, text="Results:",font=("Helvetica", 14)).place(x=700, y=90)                          #Results label
Label(root, text="Enter your function:",font=("Helvetica", 10)).place(x=25, y=100)              #Function label
Label(root, text="Enter end of range:",font=("Helvetica", 10)).place(x=25, y=150)               #Range label, w złotym podziale
Label(root, text="Enter your start point:",font=("Helvetica", 10)).place(x=25, y=200)           #Start point label
Label(root, text="Enter number of iterations:",font=("Helvetica", 10)).place(x=25, y=250)       #Number ob iterations label


Label(root, text="Choose predefined functions:",font=("Helvetica", 10)).place(x=25, y=300)      #Predefined functions label
Label(root, text="Selected options:",font=("Helvetica", 10)).place(x=25, y=400)      #Selected options label

Label(root, text="Minimum:",font=("Helvetica", 10)).place(x=600, y=150)      #Minimum
Label(root, text="Value of function:",font=("Helvetica", 10)).place(x=600, y=200)      #Value of functions
Label(root, text="Stop criterium:",font=("Helvetica", 10)).place(x=600, y=250)         #Stop criterium

#Function field

equation_Box = Entry(root, width=50)
equation_Box.place(x=175,y=101)

#Range field

range_Box = Entry(root, width=50)
range_Box.place(x=175,y=151)

#Start point field

startPoint_Box = Entry(root, width=50)
startPoint_Box.place(x=175,y=201)

#Number of iterations field

iterations_Box = Entry(root, width=48)
iterations_Box.place(x=188,y=251)


#Drop down box

def display_selected(choice):

    global choiceVar
    choiceVar = variable.get()
    #print(choiceVar)

options = ['-(2*X^2 - 1.05*X^4 + (1/6)*X^6 + X*Y + Y^2)',
           '(X-4)^2 + (X - Y^2)^2',
           '4*X^2 - 2.1*X^4 + (1/3)*X^6 + X*Y - 4*Y^2 + 4*Y^4',
           'Funkcja4',
           "0 - (X-4)^2 - (X -Y^2)^2 ",
           "-((X-4)^2 + (Y - 2)^2)"]

variable = StringVar()
variable.set(options[0])

# creating widget
dropdown = OptionMenu(
    root,
    variable,
    *options,
    command=display_selected
)

dropdown.place(x=225, y=295)

#Accept Button

def Accept():

    global chosen

    if equation_Box.get() == "":
        chosen = "Your options are - Equation: " + variable.get() + ", Range: " + range_Box.get()  + ", Start point: " + startPoint_Box.get() + ", Number of iterations: " + iterations_Box.get()
    else:
        chosen = "Your options are - Equation: " + equation_Box.get() + ", Range: " + range_Box.get() + ", Start point: " + startPoint_Box.get() + ", Number of iterations: " + iterations_Box.get()

    global myLabel
    myLabel = Label(root, text=chosen)
    myLabel.place(x=25,y=450)

def clear():
    chosen = "                                                                                                                                                                                        " \
             "                                                                                                                                       "
    myLabel = Label(root, text=chosen)
    myLabel.place(x=25, y=450)


    equation_Box.delete(0, 'end')
    range_Box.delete(0, 'end')
    startPoint_Box.delete(0, 'end')
    iterations_Box.delete(0,'end')



def play():
    chosen = "                                                                                                                                                                                        " \
             "                                                                                                                                       "
    myLabel = Label(root, text=chosen)
    myLabel.place(x=25, y=450)
    Accept()

def DownloadParameters():

    global FunctionVar
    global RangeVar
    global StartPointVar
    global IterationsVar
    global FunctionVarFloat

    global givenExpression
    global initialPoint
    global L
    global intervalLength

    #Sprawdzenie czy podana jest funkcja z boxa czy z rozwijanego menu

    FunctionVarBox = equation_Box.get()
    FunctionVarBox = FunctionVarBox.replace("^","**")
    FunctionDropDownMenu = variable.get()
    FunctionDropDownMenu = FunctionDropDownMenu.replace("^","**")


    if FunctionVarBox == "":
        FunctionVar = FunctionDropDownMenu
    else:
        FunctionVar = FunctionVarBox

    FunctionVarFloat = FunctionVar.strip("\'")
    givenExpression = FunctionVar

    RangeVar = range_Box.get()
    StartPointVar = startPoint_Box.get()
    IterationsVar = iterations_Box.get()

    L = IterationsVar
    intervalLength = RangeVar

    initialPoint = [4.5, -1]
    initialPoint = []
    strInitialPoint = StartPointVar
    strInitialPoint = strInitialPoint.replace("[" , "")
    strInitialPoint = strInitialPoint.replace("]" , "")

    list = strInitialPoint.split(",")
    print(list)
    for i in range(len(list)):
        initialPoint.append(float(list[i]))

    print("Initial point: ")
    print(initialPoint)
    print("Initial point: ")
    print(len(initialPoint))


############################### Charts ########################################


def f(X,Y):         #Preparing for plotting

    global f
    global Z
    global tmp

    feature_x = np.linspace(-10.0, 10.0, 1000)
    feature_y = np.linspace(-10.0, 10.0, 1000)

    # Creating 2-D grid of features

    [X, Y] = np.meshgrid(feature_x, feature_y)


    f1 = eval(FunctionVar)
    Z = []
    tmp = []
    Z.append(f1)

    for e1 in Z:
        for e2 in e1:
            tmp.append(e2)


##############Test3D

def Prepare3DData(X,Y):

    global Value3DFunction
    Value3DFunction = eval(FunctionVar)

    return Value3DFunction


#def plotContourf():



def plot2D():
    feature_x = np.linspace(-10.0, 10.0, 1000)
    feature_y = np.linspace(-10.0, 10.0, 1000)

    [X, Y] = np.meshgrid(feature_x, feature_y)

    fig, ax = plt.subplots(1, 1)

    f(X,Y)

    ax.clear()
    chart = ax.contourf(X, Y, tmp, levels=30)

    ax.set_title('Contour Plot')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.colorbar(chart)

    ######################## Creating points, tutaj mozesz dorzucić te punkty kolejne ########################

    # X = np.array([1])
    # Y = np.array([1])
    # plt.scatter(X, Y, color='red')
    plt.show()



def plot3D():

    X=np.array([-3,-2,-1,0,1,2,3])
    Y=X
    X,Y=np.meshgrid(X,Y)

    Prepare3DData(X, Y)

    fig = plt.figure()
    axes = fig.gca(projection="3d")

    axes.plot_surface(X,Y,Value3DFunction,cmap="viridis")

    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_zlabel('Z')
    axes.set_title('3D Plot')

    plt.contour(X,Y,Value3DFunction,cmap="viridis")
    plt.show()


def plotAll():

    plot2D()
    plot3D()

def Results():      # draw charts and calculate results

    DownloadParameters()
    plotAll()              #!!!!!!!!!!!!!!

    algorithm = OptimizationAlgorithm(givenExpression, L, initialPoint, intervalLength)
    pointList = algorithm.runAlgorithm()
    optPlace = pointList[-1]
    optValue = OptimizationAlgorithm.functionExample(givenExpression, optPlace)


    FunctionValueLabel = Label(root, text=optPlace)          #Tutaj możesz przypisać rezultaty jakie zwraca program
    FunctionValueLabel.place(x=700, y=150)

    MinimumLabel = Label(root, text=optValue)
    MinimumLabel.place(x=700, y=200)


################ Buttony ####################

AcceptButton = Button(root, text="Accept function and parameters",command=play)
AcceptButton.place(x=250,y=500)

#Clear Button

ClearButton = Button(root, text="Clear",command=clear)
ClearButton.place(x=525,y=500)

#Calculate Button - tutaj w sumie do zrobienia, ale trzeba by wrzucić jakąś funkcje tutaj, która by startowała po prostu, narazie rysuje wykresy

CalculateButton = Button(root, text="Calculate",command=Results)
CalculateButton.place(x=650, y=500)



root.mainloop()