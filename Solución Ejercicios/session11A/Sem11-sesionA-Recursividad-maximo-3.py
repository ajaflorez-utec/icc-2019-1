""" Funcion recursiva para hallar el numero maximo
de una lista"""

def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]
i=0
x=int(input("Ingrese un entero (termine con 0): "))
a=list()
while x != 0:
    a.append(x)
    i=i+1
    x=int(input("Ingrese otro numero (termine con 0): "))

print("el numero maximo es: ", Max(a))

