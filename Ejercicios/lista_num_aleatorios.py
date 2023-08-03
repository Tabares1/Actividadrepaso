def lista_num_aleatorios():
    """Crear un programa que genere una lista de números aleatorios y los imprima en pantalla."""
    import random
    lista = []
    """Se crea un ciclo for para añadir en el vector los valores aleatorios de para lista"""
    for i in range (0,10):
        lista.append(random.randint(0,99))
        i = i+1

    print(lista)
