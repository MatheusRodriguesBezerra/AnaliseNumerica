import math

def a(x):
    resultado = math.pow(x,2) + math.sin(6*x)
    return resultado

x0, x1, x2, x3, x4, x5, x6, x7 = -1, -5/7, -3/7, -1/7, 1/7, 3/7, 5/7, 1

listax = [x0, x1, x2, x3, x4, x5, x6, x7]
listafx = []

for i in listax:
    listafx.append(a(i))

i = 0
print("(xi, f(xi))")
while i < 8:
    print("(%.3f, %.8f)" % (listax[i], listafx[i]))
    i = i+1
