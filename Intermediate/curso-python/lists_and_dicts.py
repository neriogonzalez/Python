def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Nerio", "lastname": "Gonzalez"}

    super_list = [
        {"firstname": "Nerio", "lastname": "Gonzalez"},
        {"firstname": "Enrique", "lastname": "Gotera"},
        {"firstname": "Desiree", "lastname": "Larrea"},
        {"firstname": "Carolina", "lastname": "Sanchez"},
    ]

    super_dict = {
        "natural": [1, 2, 3, 4, 5],
        "integer": [-1, -2, -3, -4, -5, 0],
        "floating": [-1.1, -2.2, -3.3, -4.4, -5.5, 0, 1.1, 2.2, 3.3, 4.4, 5.5],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for value in super_list:
        for key, valor in value.items():
            print(key, "-", valor)


if __name__ == "__main__":
    run()
