class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando en la bicicleta')


def main():
    persona = Persona('Nerio')
    persona.avanza()
    ciclista = Ciclista('Andrés')
    ciclista.avanza()


if __name__ == '__main__':
    main()
