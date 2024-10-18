import unittest

def suma(a, b):
    return a + b

def verificar_suma(a, b, valor_esperado):
    resultado = suma(a, b)
    if resultado == valor_esperado:
        return resultado
    else:
        return "Error"

class TestSuma(unittest.TestCase):

    def test_suma_positivos(self):
        resultado = verificar_suma(2, 3, 5)
        self.assertEqual(resultado, 5)
        print(f"Resultado de 2 + 3: {resultado}")

    def test_suma_negativos(self):
        resultado = verificar_suma(-1, -1, -2)
        self.assertEqual(resultado, -2)
        print(f"Resultado de -1 + -1: {resultado}")

    def test_suma_positivo_negativo(self):
        resultado = verificar_suma(5, -3, 2)
        self.assertEqual(resultado, 2)
        print(f"Resultado de 5 + (-3): {resultado}")

    def test_suma_fallo(self):
        resultado = verificar_suma(1, 1, 3)  
        self.assertEqual(resultado, "Error")
        print(f"Resultado de 1 + 1: {resultado}")

if __name__ == '__main__':
    unittest.main()
