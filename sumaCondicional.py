'''DADOS DOS NUMEROS INTRODUCIDOS POR TECLADO SE CALCULA SU SUMA SI:
A) LOS DOS SON PARES, B) EL PRIMERO ES MENOR QUE 50, C) EL SEGUNDO ESTÁ ENTRE [100-500]'''


def condicionesSuma(primerNum, segundoNum):
    if primerNum % 2 == 0 and segundoNum % 2 == 0 and primerNum < 50 and segundoNum >= 100 and segundoNum <= 500:
        return True
    else:
        return False

primerNumero = int(input('Introduce el primer numero. '))
segundoNumero = int(input('Introduce el segundo numero. '))

if condicionesSuma(primerNumero, segundoNumero):
    print('La suma de los dos numeros es', primerNumero + segundoNumero)
else:
    print('No se cumple alguna de las condiciones')

## CASOS TEST ##

if __name__ == '__main__':

    numerosTest = [[4, 3, False], [4, 100, True], [4, 500, True],
                   [50, 100, False], [50, 500, False], [30, 102, True],
                   [20, 30, False], [20, 101, False], [21, 104, False]]

    for numeros in numerosTest:
        if(condicionesSuma(numeros[0], numeros[1])):
            print('OK condiciones')
        else:
            print('FAIL condiciones')
