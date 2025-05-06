# Gestión de Partidas de Ajedrez con Tableros y Movimientos

Este proyecto implementa un sistema en Python para la gestión de partidas de ajedrez y simular el movimiento de las piezas en el tablero.

## Funcionalidades principales

- **Cambio de turno**: Permitimos el cambio de fichas blancas a fichas negras cuando acabe el turno correspondiente.
- **Movimiento de las piezas**: Se pueden mover todas las piezas del tablero.
- **Captura de las piezas**: Las piezas desaparecen del tablero cuando son capturadas por otras del color contrario.
- **Lógica de jaque y jaque-mate**: Implementamos estos conceptos característicos del ajedrez.

## Estructuras de datos utilizadas

- **Matriz bidimensional 8x8**: Simula el tamaño del tablero con sus 64 casillas.
- **Lista**: Cada fila es una lista que almacena las piezas que se encuentran en ella.
- **Tupla**: Almacena las coordenadas de la casilla origen y de la casilla destino.

## Requisitos

- Python 3.7 o superior

## Ejecución

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/gestion-ajedrez.git
   cd gestion-ajedrez

   ```

2. Ejecuta el programa

   ```bash
   python tablero.py

   ```

3. Sigue las instrucciones del menú interactivo
