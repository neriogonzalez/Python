def run():
    # and i % 6 == 0 and len(i) == 5) and i % 9 == 0]
    valor = [i for i in range(1, 10000) if (
        i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]

    print(valor)


if __name__ == '__main__':
    run()
