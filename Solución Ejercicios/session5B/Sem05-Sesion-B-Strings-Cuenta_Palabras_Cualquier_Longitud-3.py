contador = 0
coincidencias=0
parrafo=input("ingrese parrafo:")
LP = len(parrafo)
buscada = input("palabra a buscar:")
L1= len(buscada)

for i in range (LP):
    ##comparar primera letra
    if (parrafo[i] == buscada[0]) and (i+L1 <=LP):
          ##sólo si son iguales las primeras letras, comparamos el resto:
          for j in range (L1):
                   if parrafo [i+j]== buscada[j]:
                       #print(parrafo [i+j], "-", buscada[j])
                       coincidencias=coincidencias+1
                   else:
                       coincidencias=0
          ## si las coincidencias resultan iguales a la longitud, incremento contador.
          #print("coincidencias: ",coincidencias )
          if coincidencias == L1:
              contador= contador+1
              #print (contador)
              coincidencias=0
print(contador)



