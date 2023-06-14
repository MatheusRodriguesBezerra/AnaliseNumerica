import math

k = 1

f = 1 / (k * 3**k)

eps = 10 ** -3
F=f
print(f)

while abs(f) >= abs(eps):
    k = k + 1
    f = 1 / (k * 3**k)
    F = F + f
    print(f)

print(F)