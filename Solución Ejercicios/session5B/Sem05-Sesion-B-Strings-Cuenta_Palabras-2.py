contador = 0
parrafo=input("ingrese parrafo:")
buscada = input("palabra de tres letras a buscar:")

for i in range (len(parrafo)):
      if parrafo[i] == buscada[0] and parrafo[i+1] == buscada[1] and parrafo[i+2] == buscada[2]:
          contador = contador +1
print (contador)


