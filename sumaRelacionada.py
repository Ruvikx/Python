'''DADOS 3 NUMEROS INTRODUCIDOS POR TECLADO DETERMINAR SI SE CUMPLE QUE
NUM1 = NUM2 + NUM3 O NUM2 = NUM1 + NUM3 O NUM3 = NUM1 + NUM2'''


def sumaRelacionada(primerNum, segundoNum, tercerNum):
    if primerNum == segundoNum + tercerNum or segundoNum == primerNum + tercerNum or tercerNum == primerNum + segundoNum:
        return True
    else:
        return False

primerNumero = int(input('Introduce el primer numero. '))
segundoNumero = int(input('Introduce el segundo numero. '))
tercerNumero = int(input('Introduce el tercer numero. '))

if sumaRelacionada(primerNumero, segundoNumero, tercerNumero):
    if primerNumero == segundoNumero + tercerNumero:
        print('Se cumple que N1 = N2 + N3')
    elif segundoNumero == primerNumero + tercerNumero:
        print('Se cumple que N2 = N1 + N3')
    else:
        print('Se cumple que N3 = N1 + N2')
else:
    print('Los numeros no cumplen la condicion')

## CASOS TEST ##

if __name__ == '__main__':

    numerosTest = [[2, 2, 4], [4, 2, 1], [-2, 6, 4], [5, 3, 2], [1, 2, 6], [-1, -1, 1], [0, 3, 3]]

    for numeros in numerosTest:
        if sumaRelacionada(numeros[0], numeros[1], numeros[2]):
            print('OK')
        else:
            print('FAIL')
