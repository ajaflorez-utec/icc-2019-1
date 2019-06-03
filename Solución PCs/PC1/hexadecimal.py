decimal = int(input("Decimal: "))
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

print("Hexadecimal: ", hexadecimal)