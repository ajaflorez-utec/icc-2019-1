temperatura = [["Lima", 17, 18, 16, 20, 18],
  ["Arequipa",	9,	8,	9,	10,	9],
  ["Cusco",	7,	5,	6,	6,	7],
  ["Tacna",	15,	14,	16,	14,	15],
  ["Trujillo",	22,	23,	21,	22,	24],
  ["Puno",	1,	-5,	-1,	0,	-2]]

baja = temperatura[0][1]
fila_baja = 0
alta = temperatura[0][1]
fila_alta = 0
filas = len(temperatura)
for fila in range(0, filas):
  suma = 0
  columnas = len( temperatura[fila] )
  for columna in range(1, columnas):
    suma += temperatura[fila][columna]
    if alta < temperatura[fila][columna]:
      alta = temperatura[fila][columna]
      fila_alta = fila
    if baja > temperatura[fila][columna]:
      baja = temperatura[fila][columna]
      fila_baja = fila
  promedio = suma / (columnas - 1)
  print( temperatura[fila][0], ": ",promedio)
  
print("Temperatura más alta:", temperatura[fila_alta][0], " : ", alta)
print("Temperatura más baja:", temperatura[fila_baja][0], " : ", baja)