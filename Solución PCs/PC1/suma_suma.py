n = int(input("n: "))
y = 0.0
if n >= 1:
  for x in range(1, n + 1):
    numero = 0
    for z in range(x, n + 1):
      numero += (z * 2)
    y += ((x ** 2) / 2) + (numero / (x ** 3))
  print("y:", round(y, 2) )
else:
  print("error")