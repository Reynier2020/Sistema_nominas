from datetime import date
from medicamento_controlado import MedicamentoControlado
import unittest


class TestMedicamentoControlado(unittest.TestCase):
    def setUp(self):
        self.med_con1 = MedicamentoControlado('Enalapril', 20, 'tableta', 7.55, date(2022, 5, 10), 'Medicina Interna', 60)
        self.med_con2 = MedicamentoControlado('Hidroclorotiazida', 25, 'tableta', 0.30, date(2021, 2, 12), 'MGI', 60)
        self.med_con3 = MedicamentoControlado('Salbutamol', 100, 'aerosol', 3.20, date(2024, 10, 24), 'MGI', 1)
        self.med_con4 = MedicamentoControlado('Tioridazina', 25, 'tableta', 0.80, date(2023, 4, 3), 'Psiquiatría', 90)
        self.med_con5 = MedicamentoControlado('Metformina', 500, 'tableta', 3.60, date(2023, 7, 17), 'Endocrinología', 90)
    
    def test_init(self):
        self.assertIsNotNone(self.med_con1)
        self.assertIsNotNone(self.med_con2)
        self.assertIsNotNone(self.med_con3)
        self.assertIsNotNone(self.med_con4)
        self.assertIsNotNone(self.med_con5)
    
    def test_properties_super(self):
        self.assertEqual(self.med_con1.nombre, 'Enalapril')
        self.assertEqual(self.med_con2.precio_unitario, 0.30)
        self.assertEqual(self.med_con3.forma_presentacion, 'aerosol')
        self.assertEqual(self.med_con4.fecha_vencimiento, date(2023, 4, 3))
        self.assertEqual(self.med_con5.mg_contiene, 500)

        self.med_con1.forma_presentacion = 'spray'
        self.assertEqual(self.med_con1.forma_presentacion, 'spray')
        self.med_con2.fecha_vencimiento = date(2022, 9, 28)
        self.assertEqual(self.med_con2.fecha_vencimiento, date(2022, 9, 28))
        self.med_con3.mg_contiene = 50
        self.assertEqual(self.med_con3.mg_contiene, 50)
        self.med_con4.precio_unitario = 1.60
        self.assertEqual(self.med_con4.precio_unitario, 1.60)
        self.med_con5.nombre = 'Metformin'
        self.assertEqual(self.med_con5.nombre, 'Metformin')

    def test_property_especialidad_doctor_receta(self):
        self.assertEqual(self.med_con1.especialidad_doctor_receta, 'Medicina Interna')
        self.assertEqual(self.med_con2.especialidad_doctor_receta, 'MGI')
        self.assertEqual(self.med_con3.especialidad_doctor_receta, 'MGI')
        self.assertEqual(self.med_con4.especialidad_doctor_receta, 'Psiquiatría')
        self.assertEqual(self.med_con5.especialidad_doctor_receta, 'Endocrinología')

        self.med_con4.especialidad_doctor_receta = 'Geriatría'
        self.assertEqual(self.med_con4.especialidad_doctor_receta, 'Geriatría')
        self.med_con5.especialidad_doctor_receta = 'MGI'
        self.assertEqual(self.med_con5.especialidad_doctor_receta, 'MGI')

    def test_property_cant_max_venta(self):
        self.assertEqual(self.med_con1.cant_max_venta, 60)
        self.assertEqual(self.med_con2.cant_max_venta, 60)
        self.assertEqual(self.med_con3.cant_max_venta, 1)
        self.assertEqual(self.med_con4.cant_max_venta, 90)
        self.assertEqual(self.med_con5.cant_max_venta, 90)

        self.med_con2.cant_max_venta = 30
        self.assertEqual(self.med_con2.cant_max_venta, 30)
        self.med_con3.cant_max_venta = 2
        self.assertEqual(self.med_con3.cant_max_venta, 2)

    def test_importe(self):
        self.assertEqual(self.med_con1.importe(17), 143.35)   # 17 * 7.55 + 5 + 10
        self.assertEqual(self.med_con1.importe(0), 15)   # 0 * 7.55 + 5 + 10
        self.assertEqual(self.med_con1.importe(1), 22.55)   # 1 * 7.55 + 5 + 10
        self.assertEqual(self.med_con2.importe(5), 16.5)   # 5 * 0.30 + 5 + 10
        self.assertEqual(self.med_con3.importe(30), 111)   # 30 * 3.20 + 5 + 10
        self.assertEqual(self.med_con4.importe(15), 27)   # 15 * 0.80 + 5 + 10
        self.assertEqual(self.med_con5.importe(3), 25.80)   # 3 * 3.60 + 5 + 10
        
        self.med_con2.precio_unitario = 0.66
        self.assertAlmostEqual(self.med_con2.importe(9), 20.94)   # 9 * 0.66 + 5 + 10
        self.assertAlmostEqual(self.med_con2.importe(0), 15)   # 0 * 0.66 + 5 + 10
        self.assertAlmostEqual(self.med_con2.importe(1), 15.66)   # 1 * 0.66 + 5 + 10
        self.assertAlmostEqual(self.med_con2.importe(2), 16.32)   # 2 * 0.66 + 5 + 10
        self.assertAlmostEqual(self.med_con2.importe(23), 30.18)   # 23 * 0.66 + 5 + 10


if __name__ == '__main__':
    unittest.main()
