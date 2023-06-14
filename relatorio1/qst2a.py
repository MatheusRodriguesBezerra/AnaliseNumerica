import math

def f(eps):
    k = 1   # valor inicial de k
    s = 18 * ((math.factorial(k) ** 2) / ((k ** 2) * math.factorial(2 * k))) # fórmula da questão
    S = s # variavel para armazenar o somatório

    while s >= eps: # ciclo que interrompe de fazer somas no somatório quando o valor a ser somado é menor do que eps 
        k += 1
        s = 18 * ((math.factorial(k) ** 2) / ((k ** 2) * math.factorial(2 * k)))
        S += s # S está a armazenar as somas

    result = f'n° de termos somados => {k}     valor => {S}'
    print(result)

n = -8 # valor do 1º eps 

while n > -16:  # ciclo para imprimir com o valor do eps até -15
    f(10 ** n)  # chamada da função com o valor de cada eps pedido
    n -= 1

# o programa é bastante ineficiente no sentido dele ser obrigado a
# refazer todos os calculos toda vez que a função é chamada 

