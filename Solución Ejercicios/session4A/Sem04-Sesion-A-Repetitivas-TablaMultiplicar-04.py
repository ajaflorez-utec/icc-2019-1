numero = int(input())
contador = 1
if numero > 0:
    while(contador <= 9):
        print(numero, "x", contador, "=", numero * contador, sep = "")
        contador+=1
else:
    print("error")
