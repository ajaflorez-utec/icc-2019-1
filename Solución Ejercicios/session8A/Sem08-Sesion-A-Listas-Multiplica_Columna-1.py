matriz = [
          [12,14,4,8],
          [4,3,12,2],
          [7,11,10,5],
          [1,6,8,2],
         ]

columna=int(input())
r= False
while not r:
    N=int(input())
    if N>=1 and N<=5:
        r=True

for i in range (4):
    print(matriz[i][columna]*N)
