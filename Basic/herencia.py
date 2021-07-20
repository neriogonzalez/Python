class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == '__main__':
    rectangulo = Rectangulo(3, 4)
    print(f'El rectangulo tiene una área de {rectangulo.area()}')
    cuadrado = Cuadrado(5)
    print(f'El cuadrado tiene una área de {cuadrado.area()}')
