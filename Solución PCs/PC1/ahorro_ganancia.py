monto = int(input())
anhos = int(input())
interes = 0.045
nuevo_monto = monto
ganancia = 0
for val in range(anhos*12):
  nuevo_monto = nuevo_monto + (nuevo_monto * interes) - 3.5
ganancia = nuevo_monto - monto
print("Ganancia: ", ganancia)