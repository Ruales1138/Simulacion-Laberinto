class Console:
    def __init__(self):
        self.option: int = 0

    def print_menu(self):
        while self.option != 7:
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
            self.option = int(input('Seleccione una opción: '))


c = Console()
c.print_menu()