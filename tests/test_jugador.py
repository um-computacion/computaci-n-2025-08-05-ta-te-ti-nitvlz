import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):
    def test_creacion_jugador(self):
        j = Jugador("Marto", "X", "Jugando")
        self.assertEqual(j.nombre, "Marto")
        self.assertEqual(j.ficha, "X")
        self.assertEqual(j.estado, "Jugando")

    def test_con_ficha_cero(self):
        j = Jugador("Martin", "0", "Jugando")
        self.assertEqual(j.ficha, "0")

    def test_atributos_modificables(self):
        j = Jugador("Sebita", "X", "Jugando")
        j.nombre = "Nuevo Sebita"
        j.ficha = "0"
        j.estado = "Ganador"
        self.assertEqual(j.nombre, "Nuevo Sebita")
        self.assertEqual(j.ficha, "0")
        self.assertEqual(j.estado, "Ganador")

    def test_objetos_distintos(self):
        j1 = Jugador("Yudio", "X", "Jugando")
        j2 = Jugador("Gino", "X", "Jugando")
        self.assertIsNot(j1, j2)

if __name__ == "__main__":
    unittest.main()