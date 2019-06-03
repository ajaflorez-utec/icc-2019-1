lista = []

alumno = input()
while alumno != "Fin":
    lista.append( alumno )
    alumno = input()

print( len(lista), "alumnos registrados" )
