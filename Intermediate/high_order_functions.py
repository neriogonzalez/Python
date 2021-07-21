from functools import reduce


def run():

    my_list = [1, 2, 3, 4, 5]
    cuadrado = list(map(lambda i: i**2, my_list))
    #cuadrado = [i**2 for i in my_list]

    print(my_list)
    print(cuadrado)


def run2():  # reduce
    # se importa reduce de functools
    my_list = [2, 2, 2, 2, 2]
    cuadrado = reduce(lambda a, b: a*b, my_list)

    print(my_list)
    print(cuadrado)


if __name__ == '__main__':
    run2()
