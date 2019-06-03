def isDivisible11( numero ):
  sumaPar = 0
  sumaImpar = 0
  isPar = True
  while numero > 0:
    if isPar:
      sumaPar += (numero % 10)
      isPar = False
    else:
      sumaImpar += (numero % 10)
      isPar = True
    numero = numero // 10
  if sumaPar - sumaImpar == 0:
    return "SI"
  else:
    return "NO"

numero = int(input("Ingrese un número: "))
respuesta = isDivisible11( numero )
print("El número ", respuesta, "es divisible por 11")