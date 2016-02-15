def compararNumeros(primerNum, segundoNum):
    if primerNum > segundoNum:
        return 1
    elif segundoNum > primerNum:
        return 0
    else:
        return 2

primerNumero = input('Introduce el primer numero: ')
segundoNumero = input('Introduce el segundo numero: ')

if compararNumeros(primerNumero, segundoNumero) == 1:
    print('El primer numero(', int(primerNumero), ') es mayor que el segundo(', int(segundoNumero), ')')
elif compararNumeros(primerNumero, segundoNumero) == 0:
    print('El primer numero(', int(primerNumero), ') es menor que el segundo(', int(segundoNumero), ')')
else:
    print('Los dos numeros son iguales')

if __name__ == '__main__':

# TEST SI UN NUMERO ES MAYOR QUE EL OTRO
    testNumeros = [[10, 3], [5, 2], [2, 5], [5, 6]]

    for numeros in testNumeros:
        if compararNumeros(numeros[0], numeros[1]) == 1:
            print('OK')
        else:
            print('FAIL')

# TEST SI LOS NUMEROS SON IGUALES
    testNumeros = [[10, 3], [5, 5], [2, 2], [5, 6]]

    for numeros in testNumeros:
        if compararNumeros(numeros[0], numeros[1]) == 2:
            print('OK')
        else:
            print('FAIL')
