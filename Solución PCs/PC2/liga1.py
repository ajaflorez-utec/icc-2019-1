liga1 = [["Deportivo Municipal",	13,	5,	5,	3],
  ["Alianza Lima",	13,	5,	4,	4],
  ["Universidad César Vallejo",	13,	6,	2,	5],
  ["Universidad Técnica de Cajamarca",	13,	4,	7,	2],
  ["Deportivo Binacional",	14,	11,	0,	3],
  ["Sporting Cristal",	13,	8,	4,	1]]

filas = len(liga1)
mayor = (liga1[0][2] * 3) + (liga1[0][3])
fila_mayor = 0
menor = mayor
fila_menor = 0
for fila in range(0, filas):
  puntaje = (liga1[fila][2] * 3) + (liga1[fila][3])
  print( liga1[fila][0], ":", puntaje )
  if mayor < puntaje:
    mayor = puntaje
    fila_mayor = fila
  if menor > puntaje:
    menor = puntaje
    fila_menor = fila

print( "El equipo con el mayor puntaje: ",liga1[fila_mayor][0])
print( "El equipo con el menor puntaje: ",liga1[fila_menor][0])