import math

def f(a): # função
    resultado = a * math.cos(a) - math.log(a) 
    return resultado

a = 1.3 # valores do intervalo 
b = 1.4 #
eps = 5 * 10 ** -8 # valor de eps
m = a
vfa = f(a)
ninteracoes = 0
erroiter = abs(b-a)

while erroiter > eps:
    ninteracoes = ninteracoes + 1
    m = (a+b) / 2
    if f(m) == 0:
        erroiter = 0

    if f(m) * vfa < 0:
        b = m
    else:
        a = m
    erroiter = erroiter/2


resultado = f'valor aproximado: {m}   \nerro absoluto: {erroiter} \nnúmero de interações: {ninteracoes}'
print(resultado)