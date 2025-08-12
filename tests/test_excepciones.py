import unittest
from src.excepciones import PosOcupadaException, Ganador, Empate

class TestExcepciones(unittest.TestCase):
    def test_posicion_ocupada_excepcionn(self):
        with self.assertRaises(PosOcupadaException):
            raise PosOcupadaException()

    def test_ganador_excepcion(self):
        with self.assertRaises(Ganador):
            raise Ganador()

    def test_empate_excepcion(self):
        with self.assertRaises(Empate):
            raise Empate()

    def test_son_subclases_de_excepcion(self):
        for cls in (PosOcupadaException, Ganador, Empate):
            self.assertTrue(issubclass(cls, Exception))

if __name__ == "__main__":
    unittest.main()