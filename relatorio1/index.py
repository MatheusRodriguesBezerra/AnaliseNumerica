import math
def bm():
    s = 1
    k = 1
    while(k<21):
        s = s + (1 / math.factorial(k))
        erroabs = abs((math.e) - s)
        result = f'para m = {k}, o valor de s é {s} o erro absoluto é {erroabs}'
        print(result)
        k = k + 1
bm()

#poderiamos terusado programas em recursão 
