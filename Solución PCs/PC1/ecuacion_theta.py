n = int(input())
theta = int(input())
y = 0
if n >= 1:
  if n >= theta:
    print("error")
  else:
    for x in range(1, n+1):
      y = y + (x ** 3) + (theta / (x - theta))
    print(y)
else:
  print("error")