def convertir_grados():
    """Crear una función que convierta grados Fahrenheit a grados Celsius"""
    fahrenheit = int(input('Ingrese los grados en Fahrenheit'))
    """Se usa la formula de conversión para sacar los grados celsius"""
    Celcius = (fahrenheit - 32) * 5/9

    mensaje = f'La temperatura en fahrenheit en celsius es {Celcius}°'

    print(mensaje)