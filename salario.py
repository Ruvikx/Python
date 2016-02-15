'''Calcular lo que tiene que cobrar un empleado
sabiendo que se le tiene que aplicar al sueldo una retención del 20%'''


def calcularSalario(salarioBruto):
    RETENCION = 0.2
    return salarioBruto - salarioBruto * RETENCION

## CASOS TEST ##

if __name__ == '__main__':

    salarios = [[1000, 800], [1200, 960], [900, 720], [1300, 1040]]

    for salario in salarios:
        if calcularSalario(salario[0]) == salario[1]:
            print('OK')
        else:
            print('FAIL')
