import math

a = 1
b = 2
fa = math.e**a
fb = math.e**b
x = [1, 1.25, 1.5, 1.75, 2]
h = 0.25
resultado = 0
i = 0
while i < 4:
    resultado = resultado + (((x[i+1]-x[i])/2) * ((math.e**x[i]) + (math.e**x[i+1])))
    i = i + 1
erro = ((h*h) / 12) * (math.e**2)

print(resultado)
print(erro)