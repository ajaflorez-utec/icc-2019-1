""" programa que eleva un numero a un exponente"""
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Ingrese la base: "))
exp=int(input("Ingrese el exponente: "))
print("Resultado:",power(base,exp))
