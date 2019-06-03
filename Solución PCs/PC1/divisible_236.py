numero = int(input())
suma = 0
divisible2 = False
divisible3 = False
if numero % 2 == 0:
  divisible2 = True
  print("divisible por 2")

while numero > 0:
  suma += (numero % 10)
  numero = numero // 10
if suma % 3 == 0:
  divisible3 = True
  print("divisible por 3")

if divisible2 and divisible3:
  print("divisible por 6")
elif not divisible2 and not divisible3:
  print("por ninguno")
