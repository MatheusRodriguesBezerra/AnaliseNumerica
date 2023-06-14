import math

#função recursiva
def recursao(p: int) -> float:
    if p > 0:
        resultado = 1 / math.factorial(p)
        return resultado + recursao(p - 1)
    else:
        return 0


recursao(20)