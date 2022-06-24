def multiplicar(*args):
    print("Estoy en la operación multiplicar:")
    multiplicacion = 1
    for x in args:
        multiplicacion = multiplicacion  * x
    return multiplicacion

