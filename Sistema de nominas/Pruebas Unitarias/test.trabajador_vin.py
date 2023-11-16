import unittest
from Modelo.Trabajador_vin import Trabajadorvin


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.trab1 = Trabajadorvin("Nico Perez", 25, "mascculino", 7/1/2023, "Profesional", "ayudante", 75, 50)
        self.trab2 = Trabajadorvin("Paco", 42, "masculino", 15/2/3, "obrero calif", "1er ministro", 100, 5)