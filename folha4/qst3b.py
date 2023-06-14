import math

a = 0
b = 1
x = [0, 1/6, 1/3, 1/2, 2/3, 5/6, 1]
h = 1/6
resultado = 0
i = 0
while i < 6:
    resultado = resultado + (((x[i+1]-x[i])/2) * ((1 / (1 + x[i])) + (1 / (1 + x[i+1]))))
    i = i + 1
erro = ((h*h) / 12) * (b-a) * 2

print(resultado)
print(erro)