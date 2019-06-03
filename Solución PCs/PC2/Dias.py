def obtenerDias(dia, mes, ano):
  dias = 0
  if mes > 1:
    dias = 14
    for contador in range(2, mes):
      if contador == 2:
        dias += 28
      elif contador == 3 or contador == 5 or contador == 7 or contador == 8 or contador == 10 or contador == 12:
        dias += 31
      else:
        dias += 30
    dias += dia
  else:
    dias = dia - 17
  return dias

dia = int(input("Ingrese día: "))
mes = int(input("Ingrese mes: "))
ano = int(input("Ingrese año: "))

dias = obtenerDias(dia, mes, ano)
print("Dias faltantes: ", dias)