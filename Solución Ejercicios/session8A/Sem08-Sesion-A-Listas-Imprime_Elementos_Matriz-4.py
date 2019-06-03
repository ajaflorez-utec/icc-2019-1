DIVISIONES = 5
TRIMESTRES = 3
divisiones = [ "Línea Blanca", "Electrodomésticos", "Juguetería",
               "Perecibles", "Limpieza"]
ventas = [
        [450, 650, 342], [340, 487, 767], [134, 212, 354],
        [180, 464, 565], [647, 324, 232]
       ]

print("                    Trim1  Trim2  Trim3")
for i in range(DIVISIONES) :
     # Procesa la i-ésima fila.
     print("%17s"%divisiones[i], end="   ")
     for j in range(TRIMESTRES) :
           # Procesa la  j-ésima columna en la i-ésima fila
           print("%6d" % ventas[i][j], end="")
     print() # Inicia una nueva línea al final de la fila

# Cálculo del total de ventas de una fila i (Una División en particular)
# en este caso Juguetería, para todos los trimestres.
total = 0
for j in range(TRIMESTRES) :
       total = total + ventas[2][j]
print("\nEl total de ventas de la División Juguetería es: ", total)

# Cálculo del total de ventas de una columna i (Un Trimestre en particular)
# en este caso el Trimestre 2, para todas las Divisiones.
total = 0
for i in range(DIVISIONES) :
       total = total + ventas[i][1]
print("\nEl total de ventas del Trimestre 2 es: ", total)

