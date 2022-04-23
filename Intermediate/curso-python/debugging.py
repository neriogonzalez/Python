def divisores(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores


def run():

    try:
        num = int(input("Ingresa un numero: "))
        if num < 0:
            raise TypeError("Debe ingresar un valor positivo")

        else:
            print(divisores(num))
        print("termino mi programa")
    except ValueError:
        print("Debes ingresar un numero")
    except TypeError as ve:
        print(ve)


if __name__ == "__main__":
    run()
