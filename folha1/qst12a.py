import math

k = 1

f = ((-1) ** k) * (k / ((5 ** k) + 10))

eps = 10 ** -4
F=f

while abs(f) >= abs(eps):
    k = k + 1
    f = ((-1) ** k) * (k / ((5 ** k) + 10))
    F = F + f
    print(F)

print(F)