from src.excepciones import Ganador, Empate, PosOcupadaException
from src.tablero import Tablero
from src.jugador import Jugador

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.jugadores = {}  

    def crear_jugador(self, nombre, ficha, estado):
        jugador = Jugador(nombre, ficha, estado)
        self.jugadores[ficha] = jugador

    def jugar_turno(self, fila_1a3, col_1a3):
        fil = fila_1a3 - 1
        col = col_1a3 - 1

        self.tablero.colocar_ficha(fil, col, self.turno)
        self.tablero.chequear_ganador()
        self.tablero.chequear_empate()

        self.turno = "0" if self.turno == "X" else "X"

    def definir_ganador(self):
        if self.turno == 'X':
            perdedor = '0'
        else:
            perdedor = 'X'
        self.jugadores[self.turno].estado = 'Ganador'
        self.jugadores[perdedor].estado = 'Perdedor'

    def definir_empate(self):
        self.jugadores['X'].estado = 'Empate'
        self.jugadores['0'].estado = 'Empate'