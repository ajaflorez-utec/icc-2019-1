""" funcion recursiva que calcula el capital a una tasa de interes i """

def capital(n,t):
    if (t==1):
        return n*(1+0.08)
    else:
        return capital(n,t-1)*1.08

n=int(input())
t=int(input())

print(capital(n,t))
