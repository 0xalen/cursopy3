#!/usr/bin/python3
from random import randint

def solicitarNumero():
    try:
        print("(Presione \'Enter\' para elegir un número al azar entre 1 y 99)")
        return int(input("Ingrese un número entero: "))
    except (ValueError, TypeError):        
        return randint(1,99)

def operaciones():
    print("Para demostrar el uso de operaciones, vamos a elegir algunos valores")
    delimitar(0)
    num1 = solicitarNumero()
    num2 = solicitarNumero()
    print("Números elegidos: ",num1," y ",num2,)
    waitForReturn(0)
    delimitar(0)
    print('''   Al igual que en otros lenguajes de programación, pueden utilizarse operaciones básicas: 
            Suma: + 
            Ej: 
            ''',num1,''' + ''',num2,''' = ''',num1+num2,'''
            Resta: - 
            Ej: 
            ''',num1,''' - ''',num2,''' = ''',num1-num2,'''
            Producto: * 
            Ej:
            ''',num1,''' * ''',num2,''' = ''',num1*num2,'''
            División: / 
            Ej:
            ''',num1,''' / ''',num2,''' = ''',num1/num2,'''
            ''')
    delimitar(1)
    waitForReturn(1)
    print('''   Vale notar que la división clásica (con "/") devuelve un número flotante.
    Para obtener sólo la parte entera del cociente, debe utilizarse la división piso (con "//")
            División piso: //
            Ej: 
            ''',num1,''' // ''',num2,''' = ''',num1//num2,'''
            
    Para calcular el resto de la division se utiliza la operación módulo (con "%").
            Módulo: %
            Ej: 
            ''',num1,''' % ''',num2,''' = ''',num1%num2,'''
            Luego la división se puede escribir como
            DIVIDENDO = DIVISOR * COCIENTE + RESTO
            num1 = num2 * (num1 // num2) + num1 % num2
            ''',num1,''' = ''',num2,''' * ''',num1//num2,''' +''',num1%num2)
    delimitar(1)
    waitForReturn(1)
    print('''   Una operación que en otros lenguajes de programación requiere importar una librería, pero que 
    en python viene de forma predeterminada, es la potencia.
            Potencia: **
             Ej: 
             ''',num1,''' ** ''',num2,''' = ''',num1**num2)
    delimitar(1)
    waitForReturn(1)
    print('''Finalmente, los paréntesis permiten establecer la prioridad de las operaciones:
            Ej: 
            ''',num1,''' + ''',num2,''' / ''',num2,''' = ''',num1+num2/num2,'''
            (''',num1,''' + ''',num2,''') / ''',num2,''' = ''',(num1+num2)/num2,'''
           ''')

def delimitar(t):
    if t == 0:
        print("#====================================================#")
    elif t == 1:
        print("#----------------------------------------------------#")
    else: 
        print("\\____________________________________________________/")

def waitForReturn(op):
    try:
        if op == 0:
            input("Presione \'Enter\' para continuar...")
        else:
            input()
    except SyntaxError:
        pass

if __name__ == '__main__':
    print("Para utilizar Python como una calculadora es necesario conocer algunos detalles: ")
    
    operaciones()
    waitForReturn(0)
