def run():
    my_list = [1, "hell0", True, 4.5]
    my_dict = {"first_name": "Nerio", "last_name": "Gonzalez"}

    super_list = [
        {"first_name1": "Nerio1", "last_name1": "Gonzalez1"},
        {"first_name2": "Nerio2", "last_name2": "Gonzalez2"},
        {"first_name3": "Nerio3", "last_name3": "Gonzalez3"}
    ]

    super_diccionario = {
        "lista1": [1, "hello1", True, 1.5],
        "lista2": [2, "hello2", True, 2.5],
        "lista3": [3, "hello3", True, 3.5]

    }

    for key, value in super_diccionario.items():
        print(key, "-", value)

    for i in super_list:
        # for key, value in i.items():
        #   print(key, "-", value)
        print(i.items())


if __name__ == '__main__':
    run()
