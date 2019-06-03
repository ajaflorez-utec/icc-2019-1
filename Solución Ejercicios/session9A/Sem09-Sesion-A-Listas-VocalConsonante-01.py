vocales = 0
consonantes = 0

nombre = input()
nombre = nombre.upper()
nombre = nombre.replace(" ", "")
lista = list(nombre)

for letra in lista:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        vocales += 1
    else:
        consonantes += 1
print(vocales, "vocales")
print(consonantes, "consonantes")
