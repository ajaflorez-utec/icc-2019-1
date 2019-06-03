#problem 1
n = int(input())
contador = 1
for x in range(n+1):
    for y in range(n+1):
        print(contador, end= " ")
        if contador < 9:
            contador = contador + 1
        else:
            contador = 1
    print()
