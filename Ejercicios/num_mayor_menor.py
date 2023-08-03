def num_mayor_menor():
    """Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada"""
    lista = []
    
   
    """se usa un ciclo while para añadir los elementos a la lista y una variable para que rompa el ciclo cuando sea diferente de si"""
    cont = 'si'
    while cont == 'si':
        lista.append(int(input('Ingrese el número' )))
        cont = str(input('Si desea continuar digite si, si no digite stop '))

    """Se crea un ciclo for para recorrer la lista y 2 variables para que guarden los datos de importancia"""

    mayor = 0
    menor = 0
    for i in lista:
        if i > mayor:
            mayor = i
        if i < menor:
            menor = i
    
    mensaje = f'El npumero mayor de la lista es {mayor} y el número menor de la lista es {menor}'

    print(mensaje)