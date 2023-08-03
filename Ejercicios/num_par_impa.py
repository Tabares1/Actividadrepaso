def num_par_impar():
    """Escribir un programa que determine si un número dado es par o impar"""
    num = int(input("Ingrese un número "))

    """Se crea un condicional para verificar si el número es par o impar dependiendo del módulo"""
    if num % 2 == 0:
        mensaje = f'El número {num} es par'
        print(mensaje)
    else:
        mensaje = f'El número {num} es impar'
        print(mensaje)