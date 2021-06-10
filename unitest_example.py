import unittest

def calcular_interes_simple(capital_inicial, tasa_interes, tiempo):
    intere = capital_inicial * tasa_interes * tiempo
    return intere

def validar_prestamo(capital):
    if capital > 500:
        tasa_interes = 5
        tiempo = 3
        return calcular_interes_simple(capital, tasa_interes, tiempo)
    else:
        return 'no preste'

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        self.assertIn('hello', ['hello', 'world'])

        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_interes_simple(self):
        self.assertEqual(calcular_interes_simple(1000, 5, 3), 15000)
        self.assertEqual(validar_prestamo(400), 'no preste')
        self.assertEqual(validar_prestamo(1000), 15000)
        self.assertEqual(validar_prestamo(2000), 30000)

if __name__ == '__main__':
    unittest.main()