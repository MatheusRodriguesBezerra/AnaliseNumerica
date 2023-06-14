def EulerEx(h):
    y,t,i = 1,0,0
    a,b = 0,1
    n = (b-a)/h
    while i <= n:
        if round(t,3) == 1:
            err = abs(y-0.6321205588286)
            return (y,err)
        y = y + h * ((t*t) - y)
        t = t + h
        i = i + 1

def main():     #função que dá a escolha do h para 0.1, 0.01 ou 0.001
    print("h = 0.100   yn = %.5f    erro = %.6f" % (EulerEx(0.1)[0],EulerEx(0.1)[1]))
    print("h = 0.010   yn = %.5f    erro = %.6f" % (EulerEx(0.01)[0],EulerEx(0.01)[1]))
    print("h = 0.001   yn = %.5f    erro = %.6f" % (EulerEx(0.001)[0],EulerEx(0.001)[1]))
main()