numero = int( input() )
archivo = input()
contador = 0

input_File = open( archivo , "w+")
while contador <= numero:
    input_File.write( str(contador) + "\n" )
    contador += 2
input_File.close()
