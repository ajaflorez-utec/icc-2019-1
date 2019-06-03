palabra = input("Ingrese Palabra: ")

palabra = palabra.lower()
if palabra == "pornografia" or palabra == "porno":
  print("bloqueado")
else:
  palabra = palabra.replace(" ", "")
  if palabra == "pornografia" or palabra == "porno":
    print("bloqueado")
  else:
    print(palabra)
    palabra = palabra.replace("0", "o")
    palabra = palabra.replace("1", "i")
    palabra = palabra.replace("4", "a")
    if palabra == "pornografia" or palabra == "porno":
      print("bloqueado")
    else:
      print(palabra)
      tamano = len(palabra)
      nuevo = ""
      for contador in range(tamano - 1, -1, -1):
        nuevo += palabra[contador]
      print(nuevo)
      if nuevo == "pornografia" or nuevo == "porno":
        print("bloqueado")
      else:
        print("Palabra sin porno")