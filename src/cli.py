from .tateti import Tateti
from .excepciones import Ganador, Empate, PosOcupadaException

def main():
    print("¡Bienvenidos al Tateti de Nitvlz!")
    juego = Tateti()
    nombre1 = input('Ingresa el nombre del jugador de la ficha X: ').strip() or "Jugador X"
    nombre2 = input('Ingresa el nombre del jugador de la ficha 0: ').strip() or "Jugador 0"
    juego.crear_jugador(nombre1, 'X', 'Jugando')
    juego.crear_jugador(nombre2, '0', 'Jugando')

# es como un while
    while True:
        print("Tablero:")
        for fila in juego.tablero.contenedor:
            print(fila)
        print(f"Turno: {juego.jugadores[juego.turno].nombre}, Ficha: {juego.turno}")
        try:
            fil = int(input("Ingrese fila (1-3): "))
            col = int(input("Ingrese col (1-3): "))
            juego.jugar_turno(fil, col)
        except PosOcupadaException as e:
            print(e)
        except Ganador as e:
            for fila in juego.tablero.contenedor:
                print(fila)
            juego.definir_ganador()
            print(f'{e}, jugador {juego.jugadores[juego.turno].nombre}')
            break
        except Empate as e:
            for fila in juego.tablero.contenedor:
                print(fila)
            juego.definir_empate()
            print(e)
            break
        except Exception as e:
            for fila in juego.tablero.contenedor:
                print(fila)
            print("Entrada inválida:Ingrese una fila y columna válidas (1-3)")

if __name__ == "__main__":
    main()