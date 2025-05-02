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

mostrar_tablero(inicializar_tablero())
