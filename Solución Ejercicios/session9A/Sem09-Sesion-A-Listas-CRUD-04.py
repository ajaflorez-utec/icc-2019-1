lista = []
for i in range(3):
    lista.append( int(input()) )

menor = min(lista)
lista.append( menor )
mayor = max(lista)
lista.insert( 0, mayor )
lista.pop(3)
lista[2] = mayor - menor

for numero in lista:
    print(numero, end = " ")
