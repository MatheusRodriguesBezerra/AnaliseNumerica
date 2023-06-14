def EulerEx(h):
    y,t,i = 1,0,0
    a,b = 0,1
    n = (b-a)/h
    while i <= n:
        print("(%.3f, %f)," % (t,y))
        y = y + h * ((t*t) - y)
        t = t + h
        i = i + 1

def main():
    n = int(input("Qual valor de h pretendes?\n1. 0.1\n2. 0.01\n3. 0.001\n"))
    if n == 1:
        return EulerEx(0.1)
    elif n == 2:
        return EulerEx(0.01)
    else:
        return EulerEx(0.001)

main()
    