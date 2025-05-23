import sys
sys.path.append('src')
from model.maze import Maze


class Console:
    def __init__(self):
        self.maze = Maze(5, 1)
        self.laberinto = self.maze.retornar_laberinto()
        self.opcion: int = 0

    def imprimir_laberinto(self):
        print()
        print(f'Turno del jugador {self.maze.turno + 1}')
        print(*self.laberinto, sep="\n")
        ruta, ruta_2 = self.maze.simular_ruta()
        print(f'Ruta 1: {ruta}')
        print(f'Ruta 2: {ruta_2}')
        if ruta == [] and ruta_2 == []:
            print('ay muchachos...')
        if self.maze.ubicacion_jugadores == []:
            self.opcion = 7

    def imprimir_menu(self):
        while self.opcion != 7:
            print('--------------------------------------------')
            print('📋 Menú Interactivo')
            print('')
            print('1️⃣  Iniciar simulación')
            print('2️⃣  Colocar bloqueos')
            print('3️⃣  Colocar trampas')
            print('4️⃣  Colocar retrasadores')
            print('5️⃣  Visualizar estado actual del laberinto')
            print('6️⃣  Ejecutar siguiente iteración')
            print('7️⃣  Salir del juego')
            print('--------------------------------------------')
            self.opcion = input('Seleccione una opción: ')
            if self.opcion == '':
                self.opcion = 0
            else:
                self.opcion = int(self.opcion)

                if self.opcion == 1 or self.opcion == 5:
                    self.imprimir_laberinto()

                if self.opcion == 2:
                    print()
                    x = int(input('Ingrese numero de fila: '))
                    y = int(input('Ingrese numero de columna: '))
                    respuesta = self.maze.colocar_boqueo(x, y)
                    if respuesta is True:
                        print('✅ Bloqueo agregado')
                    else:
                        print('❌ Casilla ocupada')
                    self.imprimir_laberinto()

                if self.opcion == 3:
                    print()
                    x = int(input('Ingrese numero de fila: '))
                    y = int(input('Ingrese numero de columna: '))
                    respuesta = self.maze.colocar_trampa(x, y)
                    if respuesta is True:
                        print('✅ Trampa agregada')
                    else:
                        print('❌ Casilla ocupada')
                    self.imprimir_laberinto()

                if self.opcion == 4:
                    print()
                    x = int(input('Ingrese numero de fila: '))
                    y = int(input('Ingrese numero de columna: '))
                    respuesta = self.maze.colocar_retrasador(x, y)
                    if respuesta is True:
                        print('✅ Retrasador agregad0')
                    else:
                        print('❌ Casilla ocupada')
                    self.imprimir_laberinto()

                if self.opcion == 6:
                    respuesta = self.maze.siguiente_iteracion()
                    self.imprimir_laberinto()
                    if respuesta is True:
                        print(f'🚩¡Jugador {self.maze.turno + 1} llego a la meta!🚩')


c = Console()
c.imprimir_menu()