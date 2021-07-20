import random


def ordernamiento_de_burbuja(lista):
    maximo = len(lista)

    for i in range(maximo):
        for j in range(0, maximo-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                #print(f'lista inicial {lista}')
    return lista


if __name__ == '__main__':
    tamano = int(input('Ingrese el tamaño de la lista: '))
    lista = [random.randint(1, 100) for i in range(tamano)]
    print(lista)
    lista_ordenada = ordernamiento_de_burbuja(lista)
    print(lista_ordenada)
