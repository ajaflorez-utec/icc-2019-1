poemas = "poemas.txt"
input_File_poemas = open( poemas , mode = "r", encoding="utf-8")

palabras = "palabras.txt"
input_File_palabras = open( palabras , mode = "w+", encoding="utf-8")

lista_palabras = []
lista_veces = []

for cadena in input_File_poemas:
    cadena = cadena.replace("\n", "")
    cadena = cadena.lower()
    lista_cadena = cadena.split(" ")

    for palabra in lista_cadena:
        if palabra in lista_palabras:
            posicion = lista_palabras.index( palabra )
            lista_veces[ posicion ] += 1
        else:
            lista_palabras.append( palabra )
            lista_veces.append( 1 )

cantidad = len( lista_palabras )
for contador in range( cantidad ):
    input_File_palabras.write( lista_palabras[contador] + " " + str(lista_veces[contador]) + "\n" )

input_File_poemas.close()
input_File_palabras.close()
