""" funcion recursiva que calcula la multiplicacion de bacterias
 """

def mult(n,t):
    if t == 1:
        return 3*n
    else:
        return mult(n,t-1)*3

n=int(input())
t=int(input())

print(mult(n,t))
