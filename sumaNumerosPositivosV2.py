'''SUMAR DOS NUMEROS SOLO SI SON POSITIVOS AMBOS E ESPECIFICANDO, EN
EL CASO DE QUE HAYA NUMEROS NEGATIVOS, CUALES SON'''


def comprobarSignoNumero(primerNum, segundoNum):
    if primerNum > 0 and segundoNum > 0:
        return True
    else:
        return False

primerNumero = int(input('Introduce primer numero. '))
segundoNumero = int(input('Introduce segundoNumero. '))

if comprobarSignoNumero(primerNumero, segundoNumero):
    print('La suma de los dos numeros es: ', primerNumero + segundoNumero)
else:
    if primerNumero < 0 and segundoNumero >= 0:
        print('No se calcula la suma porque el primer numero es negativo')
    elif primerNumero >= 0 and segundoNumero < 0:
        print('No se calcula la suma porque el segundo numero es negativo')
    else:
        print('No se calcula la suma porque los dos numeros son negativos')

## CASOS TEST ##

if __name__ == '__main__':

    testNumeros = [[3, 3], [2, -1], [2, 5], [-3, 3], [-2, 1], [2, 1]]

    for numeros in testNumeros:
        if comprobarSignoNumero(numeros[0], numeros[1]):
            print('OK')
        else:
            print('FAIL')
