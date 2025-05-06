import copy

def inicializar_tablero():
    tablero = [[None for i in range(8)] for i in range(8)]
    for i in range(8):
        tablero[1][i] = "P"  # Peones blancos
        tablero[6][i] = "p"  # Peones negros

    tablero[0][0] = tablero[0][7] = "R"  # Torres blancas
    tablero[7][0] = tablero[7][7] = "r"  # Torres negras

    tablero[0][1] = tablero[0][6] = "C"  # Caballos blancos
    tablero[7][1] = tablero[7][6] = "c"  # Caballos negros

    tablero[0][2] = tablero[0][5] = "B"  # Alfiles blancos
    tablero[7][2] = tablero[7][5] = "b"  # Alfiles negros

    tablero[0][3] = "Q"  # Dama blanca
    tablero[7][3] = "q"  # Dama negra

    tablero[0][4] = "K"  # Rey blanco
    tablero[7][4] = "k"  # Rey negro

    return tablero

def mostrar_tablero(tablero):
    print("\n    " + "   ".join(str(i+1) for i in range(8)))
    print("  +" + "---+" * 8)
    for i, fila in enumerate(tablero):
        fila_str = f"{i+1} |"
        for celda in fila:
            fila_str += f" {celda if celda else ' '} |"
        print(fila_str)
        print("  +" + "---+" * 8)

def encontrar_rey(tablero, es_blancas): #Encuentra la pieza del rey en el tablero
    rey = 'K' if es_blancas else 'k'
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == rey:
                return (i, j)
    return None

def en_jaque(tablero, es_blancas): #Comprueba si el rey se encuentra en jaque
    rey_pos = encontrar_rey(tablero, es_blancas)
    if not rey_pos:
        return False

    for i in range(8):
        for j in range(8):
            pieza = tablero[i][j]
            if pieza and pieza.isupper() != es_blancas:
                if es_movimiento_valido(pieza, (i, j), rey_pos, tablero):
                    return True
    return False

def hay_movimientos_legales(tablero, es_blancas):
    for i in range(8):
        for j in range(8):
            pieza = tablero[i][j]
            if pieza and pieza.isupper() == es_blancas:
                for x in range(8):
                    for y in range(8):
                        if es_movimiento_valido(pieza, (i, j), (x, y), tablero):
                            copia = copy.deepcopy(tablero)
                            copia[x][y] = pieza
                            copia[i][j] = None
                            if not en_jaque(copia, es_blancas):
                                return True
    return False

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

        return False

    # Movimiento de Torre
    elif pieza.lower() == 'r':
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

    # Movimiento de Caballo
    elif pieza.lower() == 'c':
        if (abs(dy), abs(dx)) in [(2, 1), (1, 2)]:
            destino_pieza = tablero[fila_destino][col_destino]
            return destino_pieza is None or destino_pieza.islower() != pieza.islower()
        return False

    # Movimiento de Alfil
    elif pieza.lower() == 'b':
        if abs(dy) != abs(dx):
            return False
        paso_y = 1 if dy > 0 else -1
        paso_x = 1 if dx > 0 else -1
        for i in range(1, abs(dy)):
            if tablero[fila_origen + i * paso_y][col_origen + i * paso_x] is not None:
                return False
        destino_pieza = tablero[fila_destino][col_destino]
        return destino_pieza is None or destino_pieza.islower() != pieza.islower()

    # Movimiento de Reina
    elif pieza.lower() == 'q':
        return es_movimiento_valido('r' if pieza.islower() else 'R', origen, destino, tablero) or \
               es_movimiento_valido('b' if pieza.islower() else 'B', origen, destino, tablero)

    # Movimiento de Rey
    elif pieza.lower() == 'k':
        if abs(dy) <= 1 and abs(dx) <= 1:
            destino_pieza = tablero[fila_destino][col_destino]
            return destino_pieza is None or destino_pieza.islower() != pieza.islower()
        return False

    return False

def mover_pieza(tablero, origen, destino, turno_blancas):
    pieza = tablero[origen[0]][origen[1]]
    if not es_movimiento_valido(pieza, origen, destino, tablero):
        print("Movimiento no válido.")
        return False

    copia = copy.deepcopy(tablero)
    copia[destino[0]][destino[1]] = pieza
    copia[origen[0]][origen[1]] = None

    if en_jaque(copia, turno_blancas):
        print("No puedes hacer ese movimiento, dejarías a tu rey en jaque.")
        return False

    tablero[destino[0]][destino[1]] = pieza
    tablero[origen[0]][origen[1]] = None
    return True

def main():
    tablero = inicializar_tablero()
    turno_blancas = True

    while True:
        mostrar_tablero(tablero)
        if en_jaque(tablero, turno_blancas):
            if not hay_movimientos_legales(tablero, turno_blancas):
                print("Jaque mate. Ganan las " + ("negras" if turno_blancas else "blancas"))
                break
            else:
                print("¡Estás en jaque!")
        elif not hay_movimientos_legales(tablero, turno_blancas):
            print("Tablas por ahogado.")
            break

        print("Turno de las " + ("blancas" if turno_blancas else "negras"))
        origen = input("Origen (fila,col) o 'salir': ")
        if origen.lower() == 'salir':
            break
        destino = input("Destino (fila,col): ")

        try:
            origen = tuple(map(lambda x: int(x) - 1, origen.split(",")))
            destino = tuple(map(lambda x: int(x) - 1, destino.split(",")))

            pieza = tablero[origen[0]][origen[1]]
            if not pieza:
                print("No hay pieza en esa posición.")
                continue
            if pieza.isupper() != turno_blancas:
                print("Esa pieza no te pertenece.")
                continue

            if mover_pieza(tablero, origen, destino, turno_blancas):
                turno_blancas = not turno_blancas
        except:
            print("Entrada inválida. Usa el formato fila,col (por ejemplo: 2,1).")

if __name__ == "__main__":
    main()
