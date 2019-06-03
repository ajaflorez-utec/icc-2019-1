""" funcion recursiva que multiplica un numero por 5 """

def mult5(n):
    if n == 1:
        return 5
    else:
        return mult5(n-1) + 5

n=int(input())
print(mult5(n))
