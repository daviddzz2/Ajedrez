def inicializar_tablero():
    tablero = [[None for i in range(8)] for i in range(8)]
    for i in range(8):
        tablero[1][i] = "P"  # Peones blancos
        tablero[6][i] = "p"  # Peones negros

    tablero[0][0] = tablero[0][7] = "T"  # Torres blancas
    tablero[7][0] = tablero[7][7] = "t"  # Torres negras

    return tablero
