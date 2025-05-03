# De momento solo se pueden mover peones y torres
# Hay que implementar el movimiento de las demás piezas y la captura de piezas
# También hay que implementar la lógica de jaque y jaque mate

def inicializar_tablero():
    tablero = [[None for i in range(8)] for i in range(8)]
    for i in range(8):
        tablero[1][i] = "P"  # Peones blancos
        tablero[6][i] = "p"  # Peones negros

    tablero[0][0] = tablero[0][7] = "T"  # Torres blancas
    tablero[7][0] = tablero[7][7] = "t"  # Torres negras

    tablero[0][1] = tablero[0][6] = "C"  # Caballos blancos
    tablero[7][1] = tablero[7][6] = "c"  # Caballos negros

    tablero[0][2] = tablero[0][5] = "A"  # Alfiles blancos
    tablero[7][2] = tablero[7][5] = "a"  # Alfiles negros

    tablero[0][3] = "Q"  # Dama blanca
    tablero[7][3] = "q"  # Dama negra

    tablero[0][4] = "K"  # Rey blanco
    tablero[7][4] = "k"  # Rey negro

    return tablero

def mostrar_tablero(tablero):
    print("\n" + " " * 9 + "TABLERO DE AJEDREZ")
    print("\n    " + "   ".join(str(i+1) for i in range(8)))
    print("  +" + "---+" * 8)
    for i, fila in enumerate(tablero):
        fila_str = f"{i+1} |"
        for celda in fila:
            if celda is None:
                fila_str += "   |"
            else:
                fila_str += f" {celda} |"
        print(fila_str)
        print("  +" + "---+" * 8)

def es_movimiento_valido(pieza, origen, destino, tablero):
    fila_origen, col_origen = origen
    fila_destino, col_destino = destino
    dy = fila_destino - fila_origen
    dx = col_destino - col_origen

    if pieza is None:
        return False

    # Movimiento de Peón
    if pieza.lower() == 'p':
        direccion = 1 if pieza.isupper() else -1  # Jugador 1 hacia abajo, jugador 2 hacia arriba

        # Movimiento simple: un paso hacia adelante
        if dy == direccion and dx == 0 and tablero[fila_destino][col_destino] is None:
            return True

        if dy == direccion and abs(dx) == 1:
            destino_pieza = tablero[fila_destino][col_destino]
            if destino_pieza is not None and destino_pieza.islower() != pieza.islower():
                return True
        # Captura (no implementada aún)
        return False

    # Movimiento de Torre
    elif pieza.lower() == 't':
        if dy != 0 and dx != 0:
            return False  # Solo se mueve en línea recta

        # Comprobar si el camino está libre
        if dy == 0:  # Movimiento horizontal
            paso = 1 if dx > 0 else -1
            for j in range(col_origen + paso, col_destino, paso):
                if tablero[fila_origen][j] is not None:
                    return False

        elif dx == 0:  # Movimiento vertical
            paso = 1 if dy > 0 else -1
            for i in range(fila_origen + paso, fila_destino, paso):
                if tablero[i][col_origen] is not None:
                    return False

        # Validar si destino está vacío o tiene pieza del oponente
        destino_pieza = tablero[fila_destino][col_destino]
        if destino_pieza is None or destino_pieza.islower() != pieza.islower():
            return True

    return False

def mover_pieza(tablero, pieza, origen, destino, turno_blancas):
    fila_origen, col_origen = origen
    fila_destino, col_destino = destino

    if es_movimiento_valido(pieza, origen, destino, tablero):
        tablero[fila_destino][col_destino] = pieza
        tablero[fila_origen][col_origen] = None
        print(f"Movimiento realizado: has movido la pieza {pieza}")
        return not turno_blancas  # Cambiar turno
    else:
        print("Movimiento no válido.")
        return turno_blancas

def main():
    tablero = inicializar_tablero()
    turno_blancas = True  # Alternar entre jugadores

    print("Bienvenido al juego de Ajedrez!!")

    while True:
        mostrar_tablero(tablero)
        print("Turno de las piezas blancas (mayúsculas)." if turno_blancas else "Turno de las piezas negras (minúsculas).")

        try:
            origen = input("Ingresa la posición inicial (fila,col) o 'salir': ")
            if origen.lower() == 'salir':
                break
            destino = input("Ingresa la posición final (fila,col): ")

            origen = tuple(map(lambda x: int(x) - 1, origen.split(",")))
            destino = tuple(map(lambda x: int(x) - 1, destino.split(",")))

            pieza = tablero[origen[0]][origen[1]]
            if pieza is None:
                print("No hay pieza en esa posición.")
                continue

            if turno_blancas and not pieza.isupper():
                print("Es turno de las piezas blancas.")
                continue
            elif not turno_blancas and not pieza.islower():
                print("Es turno de las piezas negras.")
                continue

            turno_blancas = mover_pieza(tablero, pieza, origen, destino, turno_blancas)

        except Exception as e:
            print("Entrada inválida. Usa formato fila,col (por ejemplo: 1,0).")

if __name__ == "__main__":
    main()
