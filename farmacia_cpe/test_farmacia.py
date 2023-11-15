from datetime import date
from farmacia import Farmacia
from medicamento import Medicamento
from medicamento_controlado import MedicamentoControlado
import unittest


class TestFarmacia(unittest.TestCase):
    def setUp(self):
        self.med1 = Medicamento('Dipirona', 300, 'tableta', 7.0, date(2022, 12, 29))
        self.med2 = Medicamento('Ácido fólico', 1, 'tableta', 0.60, date(2023, 3, 15))
        self.med3 = Medicamento('Permetrina 1%', 110, 'loción', 14.10, date(2024, 1, 8))
        self.med4 = Medicamento('Metoclopramida', 15, 'gotas', 6.90, date(2021, 11, 30))
        self.med5 = Medicamento('Metilbromuro de Homatropina', 120, 'jarabe', 11.30, date(2022, 6, 8))

        self.med_con1 = MedicamentoControlado('Enalapril', 20, 'tableta', 7.55, date(2022, 5, 10), 'Medicina Interna', 60)
        self.med_con2 = MedicamentoControlado('Hidroclorotiazida', 25, 'tableta', 0.30, date(2021, 2, 12), 'MGI', 60)
        self.med_con3 = MedicamentoControlado('Salbutamol', 100, 'aerosol', 3.20, date(2024, 10, 24), 'MGI', 1)
        self.med_con4 = MedicamentoControlado('Tioridazina', 25, 'tableta', 0.80, date(2023, 4, 3), 'Psiquiatría', 90)
        self.med_con5 = MedicamentoControlado('Metformina', 500, 'tableta', 3.60, date(2023, 7, 17), 'Endocrinología', 90)

        self.lista_meds = [self.med1, self.med_con4, self.med3, self.med_con2, self.med5, self.med4, self.med_con5, self.med_con1, self.med_con3, self.med2]
        self.farmacia = Farmacia()

    def test_init(self):
        self.assertIsNotNone(self.farmacia)

    def test_property_lista_medicamentos(self):
        # self.fail('sin implementar')
        self.assertListEqual(self.farmacia.lista_medicamentos, [])

        self.farmacia.lista_medicamentos = self.lista_meds
        self.assertListEqual(self.farmacia.lista_medicamentos, self.lista_meds)
        self.assertIn(self.med1, self.farmacia.lista_medicamentos)
        self.assertIn(self.med_con5, self.farmacia.lista_medicamentos)

        self.farmacia.lista_medicamentos = [self.med1, self.med_con3, self.med2]
        self.assertNotEqual(self.farmacia.lista_medicamentos, [self.med2, self.med1, self.med_con3])
        self.assertCountEqual(self.farmacia.lista_medicamentos, [self.med2, self.med1, self.med_con3])
        self.assertIn(self.med2, self.farmacia.lista_medicamentos)
        self.assertNotIn(self.med_con5, self.farmacia.lista_medicamentos)

    def test_importe_compra(self):
        self.farmacia.lista_medicamentos = self.lista_meds
        self.assertIsNone(self.farmacia.importe_compra('Alprazolam', 25))

        res1 = self.farmacia.importe_compra('Dipirona', 5)
        self.assertIsNotNone(res1)
        self.assertIsInstance(res1, float)
        self.assertNotIsInstance(res1, int)
        self.assertEqual(res1, 40.0)

        self.assertAlmostEqual(self.farmacia.importe_compra('Dipirona', 10), 75.0)
        self.assertAlmostEqual(self.farmacia.importe_compra('Metoclopramida', 12), 87.80)
        self.assertAlmostEqual(self.farmacia.importe_compra('Enalapril', 20), 166.0)
        self.assertAlmostEqual(self.farmacia.importe_compra('Salbutamol', 33), 120.6)

    def test_comprar_medicamento_controlado(self):
        self.farmacia.lista_medicamentos = self.lista_meds
        self.assertIsNone(self.farmacia.comprar_medicamento_controlado('Alprazolam', 10))

        res1 = self.farmacia.comprar_medicamento_controlado('Metformina', 60)
        self.assertIsNotNone(res1)
        self.assertTrue(res1)

        self.assertTrue(self.farmacia.comprar_medicamento_controlado('Salbutamol', 1))
        self.assertTrue(self.farmacia.comprar_medicamento_controlado('Tioridazina', 80))
        
        self.assertFalse(self.farmacia.comprar_medicamento_controlado('Hidroclorotiazida', 90))
        self.assertFalse(self.farmacia.comprar_medicamento_controlado('Enalapril', 30))
        self.assertFalse(self.farmacia.comprar_medicamento_controlado('Salbutamol', 2))

        self.assertIsNone(self.farmacia.comprar_medicamento_controlado('Metoclopramida', 2))
        self.assertIsNone(self.farmacia.comprar_medicamento_controlado('Ácido fólico', 30))


if __name__ == '__main__':
    unittest.main()
