import unittest
from Modelo.Trabajador_vin import Trabajadorvin


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.trab1 = Trabajadorvin("Nico Perez", 25, "mascculino", 7/1/23, "Profesional",  )