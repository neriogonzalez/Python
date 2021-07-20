class CasillaDeVotacion:
    def __init__(self, id, pais):
        self._id = id
        self._pais = pais
        self._region = None

    @property
    def region2(self):  # ojo aquí, este es el nombre de mi variable pública, puedo colocarle cualquier nombre
        return self._region

    @region2.setter
    def set_region(self, region):
        # el nombre de la función setter puede ser cualquiera.
        # En este caso use set_region, pero también puede ser el mismo nombre de mi valiable pública

        if region in self._pais:
            self._region = region
        else:
            raise ValueError(
                f'La region {region} no está en la lista en {self._pais}')


casilla1 = CasillaDeVotacion(1, ['Caracas', 'Maracaibo'])

print(casilla1.region2)
casilla1.set_region = 'Maracaibo'
print(casilla1.region2)
