class Libro:
    def __init__(self, titulo, autor, genero, annio_creacion, es_dig, es_fis):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__annio_creacion = annio_creacion
        self.__es_dig = es_dig
        self.__es_fis = es_fis

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, text):
        self.__titulo = str(text)

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, nombre):
        self.__autor = str(nombre)

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, gennero):
        self.__genero = str(gennero)

    @property
    def annio_creacion(self):
        return self.__annio_creacion

    @annio_creacion.setter
    def annio_creacion(self, annio):
        self.__annio_creacion = int(annio)

    @property
    def es_dig(self):
        return self.__es_dig

    @es_dig.setter
    def es_dig(self, value):
        self.__es_dig = value

    @property
    def es_fis(self):
        return self.__es_fis

    @es_fis.setter
    def es_fis(self, value):
        self.__es_fis = value

    # Metodos


