import math

def maj(x):
    x0, x1, x2, x3, x4, x5, x6, x7 = -1, -5/7, -3/7, -1/7, 1/7, 3/7, 5/7, 1
    fmax = 1.653387871205 # é necessário explicar esse valor
    resultado = ((fmax) / (math.factorial(8))) * (x-x0) * (x-x1) * (x-x2) * (x-x3) * (x-x4) * (x-x5) * (x-x6) * (x-x7)
    return resultado

print(maj(0.1))
print(maj(0.9))