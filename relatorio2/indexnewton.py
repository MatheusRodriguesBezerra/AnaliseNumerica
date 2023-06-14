import math

def f(a): # função
    resultado = a * math.cos(a) - math.log(a) 
    return resultado

def flinha(a): # função
    resultado = math.cos(a) - (a * math.sin(a)) - (1/a) 
    return resultado

eps = 5 * 10 ** -8
x0 = 1.4
nmax = 10
k = 1


while k <= nmax:
    x = x0 - (f(x0) / flinha(x0))
    if (abs(x-x0) < eps) or (abs(x-x0)/abs(x) < eps) or (abs(f(x)) < eps):
        resultado = x
        erroiter = abs(x-x0)
        break
    k = k + 1
    x0 = x 

resultado = f'valor aproximado: {x}   \nerro absoluto: {erroiter} \nnúmero de interações: {k}'
print(resultado)





