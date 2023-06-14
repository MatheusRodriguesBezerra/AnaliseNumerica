import math

s = 0
n = 1
while n <= 16:
    s = ((1+(1/(10**n)))**(10**n))
    erroabs = abs(math.e - s)
    resultado = f'para n = {n}, resulta o valor {s}, o erro absoluto é {erroabs}'
    print(resultado)
    n= n + 1

