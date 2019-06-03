clave = input("Ingrese Contraseña: ")
tamano = len(clave)
if tamano < 8:
  clave += clave

nuevo = ""
nuevo_tamano = len(clave)
for contador in range(nuevo_tamano - 1, -1, -1):
  nuevo += clave[contador]
nuevo = nuevo.lower()

nuevo = nuevo.replace("i", "1")
nuevo = nuevo.replace("a", "4")
nuevo = nuevo.replace("e", "3")
nuevo = nuevo.capitalize()
nuevo += "*"
print("La nueva contraseña es: ", nuevo)