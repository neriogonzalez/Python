import time
import sys


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(99999999)
    n = 300000

    commienzo = time.time()
    factorial(n)
    final = time.time()
    print(f'factorial tarda {final-commienzo}')

    commienzo = time.time()
    factorial2(n)
    final = time.time()
    print(f'factorial recursivo tarda {final-commienzo}')
