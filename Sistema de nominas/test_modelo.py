import unittest
from UnitTest.test_conexion_datos import TestConexionDatos


if __name__ == '__main__':
    print("\nAntes de realizar las pruebas unitarias asegúrese de tener una copia de seguridad de la Base de datos, puesto que estas serán eliminadas durante las pruebas")
    selec = input("\n¿Está seguro de que desea continuar? Escriba 'S' para continuar, o 'N', o cualquier otra letra para cancelar\n")
    if selec.strip().upper() == 'S':
        print("\nRealizando pruebas unitarias: \n")
        unittest.main(verbosity=2)