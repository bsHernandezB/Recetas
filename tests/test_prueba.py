import unittest

class PruebaTestCase(unittest.TestCase):
    def setUp():
        validacion = "hola"

    def test_error(self):
        self.assertFalse(True)
