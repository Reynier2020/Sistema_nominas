class Empresa:
    pass


class Trabajador:

    def __int__(self, nombre, edad, sexo, fecha_naci, nivel_pro):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__fecha_naci = fecha_naci
        self.__nivel_pro = nivel_pro

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def set_nombre(self, value):
        return self.__nombre == value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def set_edad(self, value):
        return self.__edad == value

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def set_sexo(self, value):
        return self.__sexo == value

    @property
    def fecha_naci(self):
        return self.__fecha_naci

    @fecha_naci.setter
    def set_fecha_naci(self, value):
        return self.__fecha_naci == value

    @property
    def nivel_pro(self):
        return self.__nivel_pro

    @nivel_pro.setter
    def set_nivel_pro(self, value):
        return self.__nivel_pro == value