from datetime import date
from medicamento import Medicamento
import unittest


class TestMedicamento(unittest.TestCase):
    def setUp(self):
        self.med1 = Medicamento('Dipirona', 300, 'tableta', 7.0, date(2022, 12, 29))
        self.med2 = Medicamento('Ácido fólico', 1, 'tableta', 0.60, date(2023, 3, 15))
        self.med3 = Medicamento('Permetrina 1%', 110, 'loción', 14.10, date(2024, 1, 8))
        self.med4 = Medicamento('Metoclopramida', 15, 'gotas', 6.90, date(2021, 11, 30))
        self.med5 = Medicamento('Metilbromuro de Homatropina', 120, 'jarabe', 11.30, date(2022, 6, 8))

    def test_init(self):
        self.assertIsNotNone(self.med1)
        self.assertIsNotNone(self.med2)
        self.assertIsNotNone(self.med3)
        self.assertIsNotNone(self.med4)
        self.assertIsNotNone(self.med5)

    def test_property_nombre(self):
        self.assertEqual(self.med1.nombre, 'Dipirona')
        self.assertEqual(self.med2.nombre, 'Ácido fólico')
        self.assertEqual(self.med3.nombre, 'Permetrina 1%')
        self.assertEqual(self.med4.nombre, 'Metoclopramida')
        self.assertEqual(self.med5.nombre, 'Metilbromuro de Homatropina')

        self.med1.nombre = 'Duralgina'
        self.assertEqual(self.med1.nombre, 'Duralgina')
        self.med5.nombre = 'Novatropín'
        self.assertEqual(self.med5.nombre, 'Novatropín')

    def test_property_mg_contiene(self):
        self.assertEqual(self.med1.mg_contiene, 300)
        self.assertEqual(self.med2.mg_contiene, 1)
        self.assertEqual(self.med3.mg_contiene, 110)
        self.assertEqual(self.med4.mg_contiene, 15)
        self.assertEqual(self.med5.mg_contiene, 120)

        self.med2.mg_contiene = 5
        self.assertEqual(self.med2.mg_contiene, 5)
        self.med4.mg_contiene = 30
        self.assertEqual(self.med4.mg_contiene, 30)

    def test_property_forma_presentacion(self):
        self.assertEqual(self.med1.forma_presentacion, 'tableta')
        self.assertEqual(self.med2.forma_presentacion, 'tableta')
        self.assertEqual(self.med3.forma_presentacion, 'loción')
        self.assertEqual(self.med4.forma_presentacion, 'gotas')
        self.assertEqual(self.med5.forma_presentacion, 'jarabe')

        self.med3.forma_presentacion = 'ungüento'
        self.assertEqual(self.med3.forma_presentacion, 'ungüento')
        self.med4.forma_presentacion = 'tableta'
        self.assertEqual(self.med4.forma_presentacion, 'tableta')

    def test_property_precio_unitario(self):
        self.assertEqual(self.med1.precio_unitario, 7.0)
        self.assertEqual(self.med2.precio_unitario, 0.6)
        self.assertEqual(self.med3.precio_unitario, 14.1)
        self.assertEqual(self.med4.precio_unitario, 6.9)
        self.assertEqual(self.med5.precio_unitario, 11.3)

        self.med2.precio_unitario = 0.30
        self.assertEqual(self.med2.precio_unitario, 0.3)
        self.med5.precio_unitario = 16.80
        self.assertEqual(self.med5.precio_unitario, 16.8)

    def test_property_fecha_vencimiento(self):
        self.assertEqual(self.med1.fecha_vencimiento, date(2022, 12, 29))
        self.assertEqual(self.med2.fecha_vencimiento, date(2023, 3, 15))
        self.assertEqual(self.med3.fecha_vencimiento, date(2024, 1, 8))
        self.assertEqual(self.med4.fecha_vencimiento, date(2021, 11, 30))
        self.assertEqual(self.med5.fecha_vencimiento, date(2022, 6, 8))

        self.med1.fecha_vencimiento = date(2021, 7, 2)
        self.assertEqual(self.med1.fecha_vencimiento, date(2021, 7, 2))
        self.med3.fecha_vencimiento = date(2025, 4, 23)
        self.assertEqual(self.med3.fecha_vencimiento, date(2025, 4, 23))

    def test_importe(self):
        self.assertEqual(self.med1.importe(15), 110)   # 15 * 7 + 5
        self.assertEqual(self.med1.importe(0), 5)   # 0 * 7 + 5
        self.assertEqual(self.med1.importe(1), 12)   # 1 * 7 + 5
        self.assertEqual(self.med2.importe(20), 17)   # 20 * 0.6 + 5
        self.assertEqual(self.med3.importe(5), 75.5)   # 5 * 14.10 + 5
        self.assertEqual(self.med4.importe(10), 74)   # 10 * 6.90 + 5
        #self.assertEqual(self.med5.importe(7), 84.1)   # 7 * 11.30 + 5
        self.assertAlmostEqual(self.med5.importe(7), 84.1)

        self.med1.precio_unitario = 5.23
        self.assertEqual(self.med1.importe(12), 67.76)   # 12 * 5.23 + 5
        self.assertEqual(self.med1.importe(0), 5)   # 0 * 5.23 + 5
        self.assertEqual(self.med1.importe(1), 10.23)   # 1 * 5.23 + 5
        self.assertEqual(self.med1.importe(2), 15.46)   # 2 * 5.23 + 5

    def test_esta_vencido(self):
        self.assertFalse(self.med1.esta_vencido())
        self.assertFalse(self.med2.esta_vencido())
        self.assertFalse(self.med3.esta_vencido())
        self.assertTrue(self.med4.esta_vencido())
        self.assertTrue(self.med5.esta_vencido())
        
        self.med2.fecha_vencimiento = date(2022, 4, 13)
        self.assertTrue(self.med2.esta_vencido())
        self.med5.fecha_vencimiento = date(2022, 10, 5)
        self.assertFalse(self.med5.esta_vencido())


if __name__ == '__main__':
    unittest.main()
