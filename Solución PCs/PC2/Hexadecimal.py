def getHexadecimal( decimal ):
  hexadecimal = ""
  while decimal > 0:
    resto = decimal % 16
    decimal = decimal // 16
    if resto <= 9:
      hexadecimal = str(resto) + hexadecimal
    else:
      if resto == 10:
        hexadecimal = 'A' + hexadecimal
      elif resto == 11:
        hexadecimal = 'B' + hexadecimal
      elif resto == 12:
        hexadecimal = 'C' + hexadecimal
      elif resto == 13:
        hexadecimal = 'D' + hexadecimal
      elif resto == 14:
        hexadecimal = 'E' + hexadecimal
      else:
        hexadecimal = 'F' + hexadecimal
  return hexadecimal

decimal = int(input("Ingrese un número decimal: "))
hexadecimal = getHexadecimal( decimal )
print("El equivalente en Hexadecimal es: ", hexadecimal)