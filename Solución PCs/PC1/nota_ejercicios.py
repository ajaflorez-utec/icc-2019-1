bien = int(input())
minutos = int(input())

nota = (bien * 20) / 50

for a in range(minutos):
  nota -= (nota * 0.005)
print(nota)