from cmath import log
import math
from unittest import result

x0 = 0.12
y0 = 3.1

f = x0 ** y0

flinhax = abs((x0 ** (y0 - 1)) * y0)
flinhay = abs((x0 ** y0) * log(x0))

deltax = abs(5 * (10 ** -3))
deltay = abs(5 * (10 ** -2))

resultado = flinhax * deltax + flinhay * deltay

print(resultado)

