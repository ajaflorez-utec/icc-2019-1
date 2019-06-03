contador = 1
numero = int(input())
if numero >= 0:
    while(contador <= numero):
        print(contador * contador)
        contador+=1
else:
    print("error")
