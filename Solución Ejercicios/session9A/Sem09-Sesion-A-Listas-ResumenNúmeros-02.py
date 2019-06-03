suma = 0
lista = []

numero = int(input())
while numero > 0:
    suma += numero
    lista.append( numero )
    numero = int(input())

print( suma )
print( lista[-1] )
print( lista[0] )
print( max(lista) )
print( min(lista) )
