from src.excepciones import PosOcupadaException, Ganador, Empate

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

   
    def obtener_contenedor(self):
        return self.contenedor

    def esta_lleno(self):
        return all(c != "" for fila in self.contenedor for c in fila)

    def _validar_indices(self, fil, col):
        if not (0 <= fil <= 2 and 0 <= col <= 2):
            raise IndexError("Fila/columna fuera de rango. Por favor, ingrese un valor entre 1-3")

    def colocar_ficha(self, fil, col, ficha):
        self._validar_indices(fil, col)
        if self.contenedor[fil][col] != "":
            raise PosOcupadaException("¡Esta posicion ya está ocupada!")
        
        self.contenedor[fil][col] = ficha

    def _hay_ganador(self):
        t = self.contenedor

        for f in range(3):
            a, b, c = t[f][0], t[f][1], t[f][2]
            if a != "" and a == b == c:
                return True

        for c in range(3):
            a, b, d = t[0][c], t[1][c], t[2][c]
            if a != "" and a == b == d:
                return True

        centro = t[1][1]
        if centro != "":
            if centro == t[0][0] and centro == t[2][2]:
                return True
            if centro == t[0][2] and centro == t[2][0]:
                return True

        return False

    def chequear_ganador(self):
        if self._hay_ganador():
            raise Ganador("Ganaste!")

    def chequear_empate(self):
        if self.esta_lleno() and not self._hay_ganador():
            raise Empate("Empate!")