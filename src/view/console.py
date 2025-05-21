import sys
sys.path.append('src')
from model.maze import Maze


class Console:
    def __init__(self):
        self.maze = Maze(5, 1)
        self.laberinto = self.maze.retornar_laberinto()
        self.opcion: int = 0

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
                    print()
                    print(*self.laberinto, sep="\n")
                    ruta = self.maze.simular_ruta()
                    print(f'Ruta: {ruta}')

                if self.opcion == 2:
                    pass

                if self.opcion == 3:
                    pass

                if self.opcion == 4:
                    pass

                if self.opcion == 6:
                    self.maze.siguiente_iteracion()
                    print()
                    print(*self.laberinto, sep="\n")
                    ruta = self.maze.simular_ruta()
                    print(f'Ruta: {ruta}')


c = Console()
c.imprimir_menu()