import math

a = 0.3
b = 0.7
x = [0.3, 0.4, 0.5, 0.6, 0.7]
fx = [0.91, 0.85, 0.78, 0.70, 0.61]
h = 0.1
resultado = 0
i = 0
while i < 4:
    resultado = resultado + (((x[i+1]-x[i])/2) * (fx[i] + fx[i+1]))
    i = i + 1
erro = ((h*h) / 12) * (b-a) * 0.91

print(resultado)
print(erro)