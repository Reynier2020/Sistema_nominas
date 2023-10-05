from libro import Libro

""" saber el nombre del autor que mas libros tiene en la biblioteca
1-el titulo del libro fisico mas antiguo X
2-el genero mas abundante en formato digital X
3-cree una instancia biblioteca y cinco libros
4-modificar la clase biblioteca para que la lista de libros no se reciban por parametros y agregue los metodos
  necesarios para gestionar la lista
generos: aventura y ciencia ficcion
"""




class Biblioteca:
    def __init__(self, nombre, nombre_bibliotecario, horario):
        self.__nombre = nombre
        self.__nombre_bibliotecario = nombre_bibliotecario
        self.__horario = horario
        self.__libros_fisicos = []
        self.__libros_digitales = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, text):
        self.__nombre = str(text)

    @property
    def nombre_bibliotecario(self):
        return self.__nombre_bibliotecario

    @nombre_bibliotecario.setter
    def nombre_bibliotecario(self, nombre):
        self.__nombre_bibliotecario = str(nombre)

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, valor):
        self.__horario = str(valor)

    @property
    def libros_fisicos(self):
        return self.__libros_fisicos

    @libros_fisicos.setter
    def libros_fisicos(self, lista):
        self.__libros_fisicos = lista

    @property
    def libros_digitales(self):
        return self.__libros_digitales

    @libros_digitales.setter
    def libros_digitales(self, lista):
        self.__libros_digitales = lista

    # Metodos
    def genero_dig_abundante(self):
        counter = 0
        for libro in self.libros_digitales:
            counter += 1 if libro.genero == "aventura" else 0
        if len(self.libros_digitales) - counter < counter:
            return "aventura"
        else:
            return "ciencia ficcion"

    def insertar_libro(self, libro):
        try:
            if libro.es_fis:
                self.libros_fisicos.append(libro)
            else:
                self.libros_digitales.append(libro)
        except Exception as err:
            print(err.args)

    def eliminar_libro(self, titulo, libro):
        if libro.es_fis:
            for libro in self.libros_fisicos:
                if libro.titulo == titulo:
                    self.libros_fisicos.remove(libro)
        else:
            for libro in self.libros_digitales:
                if libro.titulo == titulo:
                    self.libros_digitales.remove(libro)

    def actualizar_libro(self):
        pass








