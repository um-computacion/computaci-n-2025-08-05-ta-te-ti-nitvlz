import unittest
from src.tablero import Tablero
from src.excepciones import PosOcupadaException, Empate, Ganador

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.t = Tablero()

    def test_init_contenedor_3x3(self):
        cont = self.t.obtener_contenedor()
        self.assertEqual(len(cont), 3)
        self.assertEqual(cont[0], ["", "", ""])
        self.assertEqual(cont[1], ["", "", ""])
        self.assertEqual(cont[2], ["", "", ""])

    def test_colocar_ficha_valida(self):
        self.t.colocar_ficha(1, 1, "X")
        self.assertEqual(self.t.obtener_contenedor()[1][1], "X")

    def test_fila_fuera_de_rango(self):
        with self.assertRaises(IndexError):
            self.t.colocar_ficha(-1, 0, "X")
        with self.assertRaises(IndexError):
            self.t.colocar_ficha(3, 0, "X")

    def test_columna_fuera_de_rango(self):
        with self.assertRaises(IndexError):
            self.t.colocar_ficha(0, -1, "X")
        with self.assertRaises(IndexError):
            self.t.colocar_ficha(0, 3, "X")

    def test_posicion_ocupada(self):
        self.t.colocar_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            self.t.colocar_ficha(0, 0, "0")

    def test_esta_lleno_false(self):
        self.assertFalse(self.t.esta_lleno())

    def test_esta_lleno_true(self):
        for f in range(3):
            for c in range(3):
                self.t.colocar_ficha(f, c, "X")
        self.assertTrue(self.t.esta_lleno())

    def test_no_ganar_con_dos_en_linea(self):
        self.t.contenedor[0] = ["X", "X", ""]
        try:
            self.t.chequear_ganador()
        except Ganador:
            self.fail("Se inició Ganador con solo dos en línea")

    def test_ganador_fila(self):
        self.t.contenedor[2] = ["0", "0", "0"]
        with self.assertRaises(Ganador):
            self.t.chequear_ganador()

    def test_ganador_columna(self):
        self.t.contenedor[0][2] = "X"
        self.t.contenedor[1][2] = "X"
        self.t.contenedor[2][2] = "X"
        with self.assertRaises(Ganador):
            self.t.chequear_ganador()

    def test_ganador_diagonal_principal(self):
        self.t.contenedor[0][0] = "X"
        self.t.contenedor[1][1] = "X"
        self.t.contenedor[2][2] = "X"
        with self.assertRaises(Ganador):
            self.t.chequear_ganador()

    def test_ganador_diagonal_secundaria(self):
        self.t.contenedor[0][2] = "X"
        self.t.contenedor[1][1] = "X"
        self.t.contenedor[2][0] = "X"
        with self.assertRaises(Ganador):
            self.t.chequear_ganador()

    def test_empate_true_sin_ganador(self):
        self.t.contenedor = [
            ["X", "0", "X"],
            ["X", "0", "0"],
            ["0", "X", "X"],
        ]
        try:
            self.t.chequear_ganador()
        except Ganador:
            self.fail("No tendría que haber ganador en este tablero")
        with self.assertRaises(Empate):
            self.t.chequear_empate()

    def test_empate_no_inicia_si_falta_una(self):
        self.t.contenedor = [
            ["X", "0", "X"],
            ["X", "0", "0"],
            ["0", "X", ""], 
        ]
        try:
            self.t.chequear_empate()
        except Empate:
            self.fail("Se inició Empate con tablero incompleto")

    def test_ultima_jugada_ganadora_no_empate(self):
    
        self.t.contenedor = [
            ["X", "0", "X"],
            ["0", "X", "0"],
            ["0", "X", ""],  
        ]
        self.t.colocar_ficha(2, 2, "X")
        with self.assertRaises(Ganador):
            self.t.chequear_ganador()
        try:
            self.t.chequear_empate()
        except Empate:
            self.fail("No tendria que haber empate si hay ganador")

if __name__ == "__main__":
    unittest.main()