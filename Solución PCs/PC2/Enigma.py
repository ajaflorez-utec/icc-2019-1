mensaje = input("Ingrese mensaje: ")
mensaje = mensaje.lower()
mensaje = mensaje.replace("a", "i")
mensaje = mensaje.replace("e", "i")
mensaje = mensaje.replace("o", "i")
mensaje = mensaje.replace("u", "i")
mensaje = mensaje.replace(",", "")
mensaje = mensaje.replace(".", "")
tamano = len(mensaje)
nuevo = ""
for letra in range(tamano - 1, -1, -1):
  nuevo += mensaje[letra]
nuevo = nuevo.capitalize()
print("Mensaje cifrado:",nuevo)