import random


def run():
    numerorandom = random.randint(1, 100)
    numero_ingresado = int(input('Adivina qué número es: '))
    while numero_ingresado != numerorandom:
        if numero_ingresado < numerorandom:
            numero_ingresado = int(
                input('No has asertado. Ingresa un número mayor:  '))
        elif numero_ingresado > numerorandom:
            numero_ingresado = int(
                input('Lo siento. Ingresa un número menor:  '))

    print('¡Ganaste! el número es: ' + str(numero_ingresado))


if __name__ == '__main__':
    run()
