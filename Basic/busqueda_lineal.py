import time
import random


def busqueda_lineal(lista, elemento):
    match = False
    for i in lista:
        if i == elemento:
            match = True
            break
    return match


if __name__ == '__main__':
    inicio = time.time()
    print(busqueda_lineal([random.randint(0, 100) for i in range(1000)], 100))
    fin = time.time()
    tiempo = fin-inicio
    print(f'tiempo: {fin-inicio}')
