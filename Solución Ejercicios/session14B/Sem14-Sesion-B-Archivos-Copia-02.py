origen = "archivito.txt"
input_File_origen = open( origen , "r")

copia = "copia.txt"
input_File_copia = open( copia , "w+")

for cadena in input_File_origen:
    input_File_copia.write( cadena )

print( "Copia realizada" )

input_File_origen.close()
input_File_copia.close()
