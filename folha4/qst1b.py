import math

a = 1
b = 2
fa = math.e**a
fb = math.e**b
resultado = (fa+fb) * ((b-a)/2)
erro = (-1/12) * math.e**2

print(erro)