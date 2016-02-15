#INTERCAMBIO DEL CONTENIDO DE DOS VARIABLES

print("Introduce primer numero")
numPrimero = input()
print("Introduce segundo numero")
numSegundo = input()

print("Primer numero:", numPrimero)
print("Segundo numero:", numSegundo)

numPrimero, numSegundo = numSegundo, numPrimero
print("Ahora el primer numero es:", numPrimero)
print("Ahora el segundo numero es:", numSegundo)
