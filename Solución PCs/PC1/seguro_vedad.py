edad = int(input())
if edad < 18 or edad > 65:
  print("edad no permitida")
else:
  if edad >= 18 and edad <= 30:
    print("Monto: ",150000)
    print("Prima: ",50)
  elif edad >= 31 and edad <= 40:
    print("Monto: ",180000)
    print("Prima: ",80)
  elif edad >= 41 and edad <= 55:
    print("Monto: ",100000)
    print("Prima: ",100)
  else:
    print("Monto: ",80000)
    print("Prima: ",200)