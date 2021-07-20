def palindromo(palabra):
    return palabra == palabra[::-1]


def run():
    print('Es un palíndromo' if palindromo(
        input('Ingresa tu palabra: ').lower().replace(' ', '')) else 'No es palíndromo')


if __name__ == '__main__':
    run()
