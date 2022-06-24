def sumar(*args):
    print("Estoy en la operacion sumar:")
    suma = 0
    for x in args:
        suma = suma + x
    return suma