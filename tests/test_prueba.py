import unittest

class PruebaTestCase(unittest.TestCase):
    def setUp(self):
        validacion = "hola"

    def test_error(self):
        self.assertFalse(False)
