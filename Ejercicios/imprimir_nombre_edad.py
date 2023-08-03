def imprimir_nombre_edad():
    """Crear un programa que pida el su nombre y edad y lo imprima en pantalla"""
    nombre = str(input('Digite su nombre '))
    edad = str(input("Digite su edad "))

    mensaje = f"Hola {nombre}, tienes {edad} años"

    print(mensaje)