import math


def logitudCircunferencia(radio):
    return 2 * math.pi * radio


def areaCircunferencia(radio):
    return math.pi * radio ** 2
    #return math.pi * pow(radio, 2)

PI = 3.141592
print("Introduce radio de la circunferencia")
radio = input()
radio = int(radio)
print("Su longitud es", logitudCircunferencia(radio))
print("Su area es", areaCircunferencia(radio))
