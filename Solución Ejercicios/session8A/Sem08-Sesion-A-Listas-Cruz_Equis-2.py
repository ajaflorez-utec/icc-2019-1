matriz=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
       ]
suma=0
for i in range(3):
    for j in range(3):
       matriz[i][j]=int(input())
caracter=input()
if caracter=="+":
    suma = suma + matriz[0][1]
    for z in range(3):
        suma = suma + matriz[1][z]
    suma = suma + matriz[2][1]

if caracter=="x":
    for i in range(3):
        suma = suma+matriz[i][i]
    suma = suma + matriz[0][2]
    suma = suma + matriz[2][0]

#Imprime matriz
for i in range(3):
    for j in range(3):
       print(matriz[i][j],end=" ")
    print()
print(suma)
