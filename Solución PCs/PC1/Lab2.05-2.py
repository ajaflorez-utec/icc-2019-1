dia = int(input())
mes = int(input())
anho = int(input())

if mes > 0 and mes < 12:
  if mes == 2:
    if dia <= 28:
      print("correcto")
    else:
      print("incorrecto")
  elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
      print("correcto")
    else:
      print("incorrecto")
  else:
    if dia <= 30:
      print("correcto")
    else:
      print("incorrecto")
else:
  print("incorrecto")
