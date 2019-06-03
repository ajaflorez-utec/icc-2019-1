import os

archivo = "empleados.txt"
# Verifica que el archivo exista antes de llamar a la función open()
if os.path.exists( archivo ):

    input_File = open( archivo , "r")
    for cadena in input_File:
        nombres, ocupacion, salariot = cadena.split(',')
        nombre, apellido = nombres.split()
        salario = int(salariot)
        print("Nombres: %s, %s\tOcupacion: %s\tSalario: $%.2f" % (apellido, nombre, ocupacion, salario))
    input_File.close()

else:
    print( "No existe el archivo" )
