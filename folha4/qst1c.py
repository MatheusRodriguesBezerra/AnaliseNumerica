import math

a = 1
b = 2
fa = math.e**a
fb = math.e**b
fmedia = math.e**((a+b)/2)
resultado = 1/6*(fa+4*fmedia+fb)
erro = ((1/32)/90)*(math.e**2)

print(erro)