#SUMAR DOS NUMEROS SOLO SI SON POSITIVOS AMBOS


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
    print('No se calcula la suma porque alguno de los dos numeros o los dos no son positivos')


## CASOS TEST ##

if __name__ == '__main__':

    testNumeros = [[3, 3], [2, -1], [2, 5], [-3, 3], [-2, 1], [2, 1]]

    for numeros in testNumeros:
        if comprobarSignoNumero(numeros[0], numeros[1]):
            print('OK')
        else:
            print('FAIL')
