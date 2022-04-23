import numbers


def run():
    # read()
    write()


def write():
    names = ["nerio", "desiree", "santiago", "bonnie", "nicolas"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for i in names:
            f.write(i)
            f.write("\n")


def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


if __name__ == "__main__":
    run()
