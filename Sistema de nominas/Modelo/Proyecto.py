class Proyecto:
    def __int__(self, nom_proy, cliente, costo, fecha_ini, fecha_culm, pciento_culm):
        self.__nom_proy = nom_proy
        self.__cliente = cliente
        self.__costo = costo
        self.__fecha_ini = fecha_ini
        self.__fecha_culm = fecha_culm
        self.__pciento_culm = pciento_culm

    @property
    def nom_proy(self):
        return self.__nom_proy

    @nom_proy.setter
    def set_nom_proy(self, value):
        return self.__nom_proy == value

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def set_cliente(self, value):
        return self.__cliente == value

    @property
    def costo(self):
        return self.__costo

    @costo.setter
    def set_costo(self, value):
        return self.__costo == value

    @property
    def fecha_ini(self):
        return self.__fecha_ini

    @fecha_ini.setter
    def set_fecha_ini(self, value):
        return self.__fecha_ini == value

    @property
    def fecha_culm(self):
        return self.__fecha_culm

    @fecha_culm.setter
    def set_fecha_culm(self, value):
        return self.__fecha_culm == value

    @property
    def pciento_culm(self):
        return  self.__pciento_culm

    @pciento_culm.setter
    def set_pciento_culm(self, value):
        return self.__pciento_culm == value