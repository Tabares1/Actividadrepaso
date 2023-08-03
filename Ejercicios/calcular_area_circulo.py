def calcular_area_circulo():
    """Escribir una función que calcule el area de un círculo dado su radio"""
    radio = int(input("Ingrese el radio del circulo"))
    area = 3.1416*(radio**2)

    mensaje = f'El área del círculo es de {area}'

    print(mensaje)