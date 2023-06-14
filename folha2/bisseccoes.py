def f(a):
    resultado = 0.123**a - a
    return resultado

a = int(input())
b = int(input())

eps = 5 * 10 ** -4

m = a
vfa = f(a)

erroiter = abs(b-a)

while erroiter > eps:
    m = (a+b) / 2
    if f(m) == 0:
        erroiter = 0

    if f(m) * vfa < 0:
        b = m
    else:
        a = m
    erroiter = erroiter/2
    print(m, erroiter)