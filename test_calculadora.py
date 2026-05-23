"""
Pruebas unitarias para el módulo calculadora.

Este archivo contiene los casos de prueba definidos con unittest
para comprobar el correcto funcionamiento de las operaciones:
suma, resta, multiplicación y división.
"""

import unittest
from calculadora import sumar, restar, multiplicar, dividir


class TestCalculadora(unittest.TestCase):
    """
    Clase de pruebas para las funciones del módulo calculadora.
    """
    def test_sumar(self):
        """
        Comprueba la función sumar con números positivos, negativos y cero.
        """
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-3, -2), -5)
        self.assertEqual(sumar(0, 5), 5)
   
   
    def test_restar(self):
        """
        Comprueba la función restar con números positivos, negativos y cero.
        """
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(-5, -2), -3)
        self.assertEqual(restar(5, 0), 5)
    
    
    def test_multiplicar(self):
        """
        Comprueba la función multiplicar con números positivos, negativos y cero.
        """
        self.assertEqual(multiplicar(4, 3), 12)
        self.assertEqual(multiplicar(-4, 3), -12)
        self.assertEqual(multiplicar(4, 0), 0)
 
 
    def test_dividir(self):
        """
        Comprueba la función dividir con números positivos, negativos y cero.
        """
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(-10, 2), -5)
        self.assertEqual(dividir(0, 5), 0)


    def test_dividir_por_cero(self):
        """
        Comprueba que la función dividir lanza un error al dividir entre cero.
        """
        with self.assertRaises(ValueError):
            dividir(10, 0)


if __name__ == "__main__":
    unittest.main()









