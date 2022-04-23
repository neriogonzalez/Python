def divisores(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores


def run():

    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisores(int(num)))
    print("termino mi programa")


if __name__ == "__main__":
    run()
