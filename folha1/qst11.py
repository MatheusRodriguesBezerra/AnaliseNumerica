import math

x = float(input())

n = 0

f = (((-1) ** n) * (x ** (2 * n))) / math.factorial(n)

eps = 10 ** -9
F=f

while abs(f) >= abs(eps):
    n = n + 1
    f = (((-1) ** n) * (x ** (2 * n))) / math.factorial(n)
    F = F + f

print(F)
valexato = math.e ** (-0.25)

print(valexato)