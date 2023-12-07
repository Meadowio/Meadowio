import math

def inpt():
    return float(input("Введите значение переменной z:"))

def x():
    return (inpt()**2) + 3

def y():
    return math.sin(4)

def f(x, y):
    print("Вычисленное решение:", x+y)
f(x(), y())
