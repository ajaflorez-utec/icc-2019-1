notas = [["Jose", 17, 18, 16, 20, 18],
  ["Lucas", 9,  8,  9,  10, 9],
  ["Rosa",  7,  5,  6,  6,  7],
  ["Carmen",  15, 14, 16, 14, 15],
  ["Rosendo", 15, 18, 16, 13, 14],
  ["Joaquin", 20, 15, 16, 9,  14]]

filas = len(notas)
suma = 0
total = 0
for fila in range(0, filas):
  baja = notas[fila][1]
  alta = notas[fila][1]
  columnas = len( notas[fila] )
  total += columnas - 1
  for columna in range(1, columnas):
    suma += notas[fila][columna]
    if alta < notas[fila][columna]:
      alta = notas[fila][columna]
    if baja > notas[fila][columna]:
      baja = notas[fila][columna]
  print("Nota más alta de", notas[fila][0], " : ", alta)
  print("Nota más baja de", notas[fila][0], " : ", baja)

promedio = suma / total
print( "Promedio de Notas: ",promedio)
