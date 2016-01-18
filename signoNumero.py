def signoNumero(num):

    if num >= 0:
        return True
    else:
        return False

numero = input("Introduce un numero. ")
signoNumero(numero)

if __name__ == '__main__':

    test = [0,1,-2,4,-3]

    for numero in test:
        if signoNumero(numero):
            print('OK')
        else:
            print('FAIL')