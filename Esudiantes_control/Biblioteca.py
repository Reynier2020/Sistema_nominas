class Biblioteca:
    def __init__(self, nombre, nombre_bibliotecario, horario):
        self.__nombre = nombre
        self.__nombre_bibliotecario = nombre_bibliotecario
        self.__horario = horario
        self.__lista_libros_fisicos = []
        self.__lista_libros_digitales = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def nombre_bibliotecario(self):
        return self.__nombre_bibliotecario

    @nombre_bibliotecario.setter
    def nombre_bibliotecario(self, valor):
        self.__nombre_bibliotecario = valor

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, valor):
        self.__horario = valor

    @property
    def lista_libros_fisicos(self):
        return self.__lista_libros_fisicos

    @lista_libros_fisicos.setter
    def lista_libros_fisicos(self, valor):
        self.__lista_libros_fisicos = valor

    @property
    def lista_libros_digitales(self):
        return self.__lista_libros_digitales

    @lista_libros_digitales.setter
    def lista_libros_digitales(self, valor):
        self.__lista_libros_digitales = valor

    def autor_mas_libros(self):
        libros_generales = self.__lista_libros_digitales.append(self.__lista_libros_fisicos)
        for libro in libros_generales:
            return max(libros_generales.autor, key = libros_generales.count)





