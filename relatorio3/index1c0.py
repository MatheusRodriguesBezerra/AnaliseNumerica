#VALOR APROXIMADO
import math

def f(x):
    resultado = math.pow(x,2) + math.sin(6*x)
    return resultado

def p(x):
    x0, x1, x2, x3, x4, x5, x6, x7 = -1, -5/7, -3/7, -1/7, 1/7, 3/7, 5/7, 1
    listax = [x0, x1, x2, x3, x4, x5, x6, x7]
    listafx = []

    for i in listax:
        listafx.append(f(i))

    I0 = ((x-x1) * (x-x2) * (x-x3) * (x-x4) * (x-x5) * (x-x6) * (x-x7)) / ((x0-x1) * (x0-x2) * (x0-x3) * (x0-x4) * (x0-x5) * (x0-x6) * (x0-x7))
    I1 = ((x-x0) * (x-x2) * (x-x3) * (x-x4) * (x-x5) * (x-x6) * (x-x7)) / ((x1-x0) * (x1-x2) * (x1-x3) * (x1-x4) * (x1-x5) * (x1-x6) * (x1-x7))
    I2 = ((x-x0) * (x-x1) * (x-x3) * (x-x4) * (x-x5) * (x-x6) * (x-x7)) / ((x2-x0) * (x2-x1) * (x2-x3) * (x2-x4) * (x2-x5) * (x2-x6) * (x2-x7))
    I3 = ((x-x0) * (x-x1) * (x-x2) * (x-x4) * (x-x5) * (x-x6) * (x-x7)) / ((x3-x0) * (x3-x1) * (x3-x2) * (x3-x4) * (x3-x5) * (x3-x6) * (x3-x7))
    I4 = ((x-x0) * (x-x1) * (x-x2) * (x-x3) * (x-x5) * (x-x6) * (x-x7)) / ((x4-x0) * (x4-x1) * (x4-x2) * (x4-x3) * (x4-x5) * (x4-x6) * (x4-x7))
    I5 = ((x-x0) * (x-x1) * (x-x2) * (x-x3) * (x-x4) * (x-x6) * (x-x7)) / ((x5-x0) * (x5-x1) * (x5-x2) * (x5-x3) * (x5-x4) * (x5-x6) * (x5-x7))
    I6 = ((x-x0) * (x-x1) * (x-x2) * (x-x3) * (x-x4) * (x-x5) * (x-x7)) / ((x6-x0) * (x6-x1) * (x6-x2) * (x6-x3) * (x6-x4) * (x6-x5) * (x6-x7))
    I7 = ((x-x0) * (x-x1) * (x-x2) * (x-x3) * (x-x4) * (x-x5) * (x-x6)) / ((x7-x0) * (x7-x1) * (x7-x2) * (x7-x3) * (x7-x4) * (x7-x5) * (x7-x6))

    listaIn = [I0, I1, I2, I3, I4, I5, I6, I7]
    i = 0
    resultado = 0
    while i < 8:
        InxFx = listafx[i] * listaIn[i]
        resultado = resultado + InxFx
        i = i + 1
    print(listafx)
    return resultado

p(0.1)
