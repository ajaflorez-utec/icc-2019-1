N=int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        if j%i == 0 or i%j == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(i)
