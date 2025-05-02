def inicializar_tablero():
    tablero = [[None for i in range(8)] for i in range(8)]
    for i in range(8):
        tablero[1][i] = "P"  # Peones blancos
        tablero[6][i] = "p"  # Peones negros

    tablero[0][0] = tablero[0][7] = "T"  # Torres blancas
    tablero[7][0] = tablero[7][7] = "t"  # Torres negras

    return tablero

def mostrar_tablero(tablero):
    print("    " + "   ".join(str(i+1) for i in range(8)))
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
