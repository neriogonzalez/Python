def run():
    # for contador in range(100):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    texto = input('Escribe in texto:  ')
    for letra in texto:
        if letra == 'o' or letra == 'O':
            break
        print(letra)


if __name__ == '__main__':
    run()