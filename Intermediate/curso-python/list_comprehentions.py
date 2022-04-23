import string


def run():
    # cuadrados = []
    # for i in range(1, 101):
    #    if i % 3 > 0:
    #        cuadrados.append(i**2)
    # print(cuadrados)

    cuadrados = [
        i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0
    ]
    print(cuadrados)


if __name__ == "__main__":
    run()
