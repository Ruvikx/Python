def areaFinca(longitud, amplitud):
    return longitud * amplitud


def perimetroFinca(longitud, amplitud):
    return 2 * (longitud + amplitud)


## CASOS TEST ##

if __name__ == '__main__':

    testArea = [[2, 3, 6], [3, 3, 9], [4, 2, 8], [2, 6, 12]]

    for medida in testArea:
        if areaFinca(medida[0], medida[1]) == medida[2]:
            print('OK calcular area')
        else:
            print('FAIL calcular area')

    testPerimetro = [[2, 3, 10], [3, 3, 12], [4, 3, 14], [2, 6, 16]]

    for medida in testPerimetro:
        if perimetroFinca(medida[0], medida[1]) == medida[2]:
            print('OK calcular perimetro')
        else:
            print('FAIL calcular perimetro')
