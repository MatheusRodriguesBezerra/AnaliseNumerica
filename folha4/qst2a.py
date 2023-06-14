import math

a = 1
b = 2
x = [1, 1.25, 1.5, 1.75]
h = 0.25
resultado = 0
i = 0
while i < 4:
    resultado = resultado + (math.e**x[i])
    i = i + 1
resultado = resultado * h
erro = (1/2)*0.25*(math.e**2)

print(erro)