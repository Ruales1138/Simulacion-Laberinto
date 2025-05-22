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
        print(*self.laberinto, sep="\n")
        ruta = self.maze.simular_ruta()
        print(f'Ruta: {ruta}')

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
                    pass

                if self.opcion == 6:
                    respuesta = self.maze.siguiente_iteracion()
                    self.imprimir_laberinto()
                    if respuesta is False:
                        print("ay muchachos...")
                    if respuesta is True:
                        print('🚩!LLegaste a la salida¡🚩')


c = Console()
c.imprimir_menu()