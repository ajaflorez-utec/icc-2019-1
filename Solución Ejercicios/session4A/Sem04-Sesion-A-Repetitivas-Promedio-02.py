suma = 0
cantidad = 0
error = False
numero = int(input())
while numero > 0:
    suma += numero
    cantidad += 1
    numero = int(input())
else:
    if numero < 0:
        error = True
        numero = int(input())
        while numero != 0:
            numero = int(input())

if error == False:
    promedio = suma / cantidad
    print( promedio )
else:
    print("error")
