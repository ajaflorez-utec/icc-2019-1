ruc = int(input("RUC: "))
monto = float(input("Monto: "))
ultimo = ruc % 10

if monto > 0:
  if ultimo == 0:
    print("Fecha: 14 de mayo")
  elif ultimo == 1:
    print("Fecha: 15 de mayo")
  elif ultimo == 2 or ultimo == 3:
    print("Fecha: 16 de mayo")
  elif ultimo == 4 or ultimo == 5:
    print("Fecha: 17 de mayo")
  elif ultimo == 6:
    print("Fecha: 18 de mayo")
  elif ultimo == 7 or ultimo == 8:
    print("Fecha: 19 de mayo")
  else:
    print("Fecha: 20 de mayo")
  
  impuesto = monto * 0.18
  print("Impuesto:", round(impuesto,1))
else:
  print("error")