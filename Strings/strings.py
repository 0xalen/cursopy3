#!/usr/bin/python3

def delimitar(t):
    if t == 0:
        print("#====================================================#")
    elif t == 1:
        print("#----------------------------------------------------#")
    else: 
        print("\\____________________________________________________/")

def waitForReturn():
    try:
        input("Presione \'Enter\' para continuar...")
    except SyntaxError:
        pass

if __name__ == '__main__':
    print("Python ofrece una amplia variedad de operaciones con cadenas de caracteres (Strings) ")
    
    operaciones()
    waitForReturn()
