from cmath import log
import math

x0 = 0.814
y0 = 0.98

w0 = x0 ** (2.01 * y0)

flinhax = abs(1 / (x0 + math.sqrt(y0)))
flinhay = abs(1 / (2 * math.sqrt(y0) * (x0 + math.sqrt(y0))))

deltax = abs(5 * (10 ** -3))
deltay = abs(5 * (10 ** -3))

resultado = flinhax * deltax + flinhay * deltay

print(w0)