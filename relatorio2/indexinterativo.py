import math

def f(a): # função
    resultado = math.e ** (-a) 
    return resultado

x0 = 0.52
eps = 5 * 10 ** -5
nmax = 1000
x1 = f(x0)
erroiter = abs(x1-x0)
i = 1

while (erroiter > eps) and (i <= nmax):
    x0 = x1
    x1 = f(x0)
    erroiter = abs(x1-x0)
    i = i + 1
    

if i > nmax:
    print("não foi possível ao fim de %d iterações encontrar a solução com o erro pretendido" % (nmax))
else:
    resultado = f'valor aproximado: {x1}   \nerro absoluto: {erroiter} \nnúmero de interações: {i}'
    print(resultado)

