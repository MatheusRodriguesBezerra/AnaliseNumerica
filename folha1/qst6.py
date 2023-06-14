x0 = 1.34
y0 = 4.02
z0 = 3.22

w0 = (x0 ** 2) / ((1.5*y0) - z0)

flinhax = 2 * x0 /(1.5*y0 * z0)
flinhay = -1.5* x0**2 / (1.5*y0 - z0)**2
flinhaz = x0**2 / (1.5*y0 - z0)**2

deltax = 5* 10**-3

resultado = flinhax * deltax + flinhay * deltax + flinhaz * deltax
print(w0)
