import unittest
from src.tateti import Tateti
from src.tablero import Tablero
from src.jugador import Jugador
from src.excepciones import Ganador, Empate, PosOcupadaException

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.game = Tateti()
        self.game.crear_jugador("Jugador1", "X", "Jugando")
        self.game.crear_jugador("Jugador2", "0", "Jugando")

    def test_init_basico(self):
        self.assertEqual(self.game.turno, "X")
        self.assertIsInstance(self.game.tablero, Tablero)

    def test_jugar_turno_mapea_1a3(self):
        self.game.jugar_turno(1, 1)
        self.assertEqual(self.game.tablero.contenedor[0][0], "X")

    def test_cambia_turno_si_no_hay_evento(self):
        self.game.jugar_turno(1, 1)  
        self.assertEqual(self.game.turno, "0")
        self.game.jugar_turno(1, 2)  
        self.assertEqual(self.game.turno, "X")

    def test_posicion_ocupada_no_cambia_turno(self):
        self.game.jugar_turno(1, 1)  
        with self.assertRaises(PosOcupadaException):
            self.game.jugar_turno(1, 1)  
        self.assertEqual(self.game.turno, "0") 

    def test_ganador_en_fila_y_estado(self):
        self.game.jugar_turno(1, 1)  
        self.game.jugar_turno(2, 1)  
        self.game.jugar_turno(1, 2)  
        self.game.jugar_turno(2, 2)  
        with self.assertRaises(Ganador):
            self.game.jugar_turno(1, 3)
        self.assertEqual(self.game.turno, "X")
        self.game.definir_ganador()
        self.assertEqual(self.game.jugadores["X"].estado, "Ganador")
        self.assertEqual(self.game.jugadores["0"].estado, "Perdedor")

    def test_empate(self):
        secuencia = [
            (1,1), (1,2), (1,3),
            (2,2), (2,1), (2,3),
            (3,2), (3,1), (3,3),
        ]
        for i, (f, c) in enumerate(secuencia):
            if i == len(secuencia) - 1:
                with self.assertRaises(Empate):
                    self.game.jugar_turno(f, c)
            else:
                self.game.jugar_turno(f, c)
        self.game.definir_empate()
        self.assertEqual(self.game.jugadores["X"].estado, "Empate")
        self.assertEqual(self.game.jugadores["0"].estado, "Empate")

if __name__ == "__main__":
    unittest.main()