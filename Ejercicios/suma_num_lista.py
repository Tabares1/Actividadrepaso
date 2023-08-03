def suma_num_lista():
    """Crear un programa que calcule la suma de los números en una lista dada"""
    lista = []
    """se usa un ciclo while para añadir los elementos a la lista y una variable para que rompa el ciclo cuando sea diferente de si"""
    cont = 'si'
    while cont == 'si':
        lista.append(int(input('Ingrese el número' )))
        cont = str(input('Si desea continuar digite si, si no digite stop' ))

    """se usa un ciclo for para recorrer la lista y la variable suma para sumar y acumular el dato"""
    suma = 0
    for i in lista:
        suma = suma + i

    mensaje = f'La suma de los números de la lista es de {suma}'

    print(mensaje)
