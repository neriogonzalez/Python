def potencia(limite):
    exponente = 0
    while exponente <= limite:
        print('2 ** ' + str(limite) + ' = ', 2**exponente)
        exponente = exponente+1


if __name__ == "__main__":
    potencia(int(input("Por favor ingrese la máxima potencia: ")))
