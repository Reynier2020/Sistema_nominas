import datetime


class Proyecto:
    _atrib_identific = 0

    def __new__(cls, *args, **kwargs):
        cls._atrib_identific += 1
        return super().__new__(cls)

    def __init__(self, nom_proy, cliente, costo, fecha_ini, fecha_culm, pciento_culm):
        self.identificador_pro = self._atrib_identific
        self.__nom_proy = nom_proy
        self.__cliente = cliente
        self.__costo = costo
        self.__fecha_ini = fecha_ini
        self.__fecha_culm = fecha_culm
        self.__pciento_culm = pciento_culm

    def __str__(self):
        return self.nom_proy

    @property
    def nom_proy(self):
        return self.__nom_proy

    @nom_proy.setter
    def nom_proy(self, value):
        self.__nom_proy = value

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def set_cliente(self, value):
        self.__cliente = value

    @property
    def costo(self):
        return self.__costo

    @costo.setter
    def costo(self, value):
        self.__costo = value

    @property
    def fecha_ini(self):
        self.__fecha_ini = datetime.date(day=int(), month=int(), year=int())
        return self.__fecha_ini

    @fecha_ini.setter
    def fecha_ini(self, value):
        self.__fecha_ini = value

    @property
    def fecha_culm(self):
        self.__fecha_culm = datetime.date(day=int(), month=int(), year=int())
        return self.__fecha_culm

    @fecha_culm.setter
    def fecha_culm(self, value):
        self.__fecha_culm = value

    @property
    def pciento_culm(self):
        return self.__pciento_culm

    @pciento_culm.setter
    def pciento_culm(self, value):
        self.__pciento_culm = value

    def es_nom_pro(self, nombre):
        return self.nom_proy == nombre
