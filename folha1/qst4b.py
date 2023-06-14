x = 2.83

flinhax = -3 * ((3 - x)**2)
flinhaxb = (-3*(x**2)) + (18*x) - 27

eps = 5 * 10 ** -3

resultado = abs(flinhax) * abs(eps)
resultado2 = abs(flinhaxb) * abs(eps)

print(flinhax)
print(resultado2)