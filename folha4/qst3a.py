import math

a = 0
b = 1
x = [0, 1/6, 1/3, 1/2, 2/3, 5/6, 1]
h = 1/6
resultado = 0
i = 0
while i < 6:
    resultado = resultado + (1 / (1 + x[i]))
    i = i + 1
resultado = resultado * h
erro = ((b-a)/2)*h*1

print(resultado)
print(erro)