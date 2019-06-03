matriz=[
        ["","",""],
        ["","",""],
        ["","",""]
       ]

# Usuario ingresa palabras a la matriz
for i in range(3):
    for j in range(3):
       matriz[i][j]=input()

#Imprime la matriz
for i in range(3):
    for j in range(3):
       print(matriz[i][j], end=" ")
    print()


for i in range(3):
    for j in range(3):
        if len(matriz[i][j])<=3:
            print(matriz[i][j],end=" ")
