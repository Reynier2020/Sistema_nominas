import unittest
from Modelo.conexion_db_gestion import RegistroDatos


class TestConexionDatos(unittest.TestCase):
    def setUp(self):
        self.datos = RegistroDatos()

        self.trab_vin1 = 'carol', 19, 'F', '20010-3-21', 'profesional', 1, 'gerente', 67, 45
        self.trab_vin2 = 'marco', '20', 'M', '20010-3-21', 'profesional', 1, 'gerente', 67, 45
        self.trab_no_vin1 = 'fernando', 22, 'M', '20010-3-21', 'profesional', 'obrero', 12, 34
        self.trab_no_vin2 = 'timy', '25', 'M', '20010-3-21', 'profesional', 'obrero', 12, 45
        self.proy1 = 'sergio', 'carlos', 9999.12, '2000-12-1', '20015-1-1', 99
        self.proy2 = 'ramirez', 'carlos', 99329.12, '2000-12-1', '20015-1-1'

    def test_insertar(self):
        with self.assertRaises(Exception):
            self.datos.insertar_vin('10000', 12)

        with self.assertRaises(Exception):
            self.datos.insertar_vin("casdda", 1323, 323)

        with self.assertRaises(Exception):
            self.datos.insetrar_no_vin('carol', 19, 'F', '20010-3-21', 'profesional', 1, 'gerente', 67, 45)

        with self.assertRaises(Exception):
            self.datos.insetrar_no_vin('ramirez', 'carlos', 99329.12, '2000-12-1', '20015-1-1')

    def test_eliminar(self):
        with self.assertRaises(Exception):
            self.datos.eliminar_vin('sd',23)
