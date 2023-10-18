from Estudiante import Estudiante
class Universidad:
    def __init__(self):
        self.__lista_est = []
        self.__lista_prof = []

    @property
    def lista_est(self):
        return self.__lista_est

    def agregar_est(self,est):
        self.__lista_est.append(est)

    def argegar_prof(self, prof):
        self.__lista_prof.append(prof)


"""e = Estudiante("poi",45,"m",575757,True)
uni = Universidad()
uni.agregar_est(e)
print(uni.lista_est)"""