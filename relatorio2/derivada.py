import sympy as sy
from sympy.interactive import init_printing
init_printing(pretty_print=True)

# Declara a variável simbólica
x = sy.Symbol('x')
# Explicita a função
funcao = x**10

# Resolve a função
resultado = sy.diff(funcao)
resultado