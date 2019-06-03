def recur_factorial(n):
   """Funcion que retorna el factorial de un numero"""
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num=int(input("Ingrese un numero: "))
if num < 0:
   print("el numero no puede ser negativo")
elif num == 0:
   print("el factorial de 0 es 1")
else:
   print("el factorial de",num,"es",recur_factorial(num))
