import random
import os
from collections import deque

# Constantes
BLOCK = 'X'
TRAP = 'T'
DELAY = 'R'
EXIT = '🏋'
PERSON = 'P'
EMPTY = '.'

# Direcciones (incluye diagonales)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

class Person:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.history_tree = {'pos': pos, 'children': []}
        self.disabled_dirs = []
        self.skip_turn = False

class Maze:
    def __init__(self, size, num_people):
        self.size = size
        self.grid = [[EMPTY for _ in range(size)] for _ in range(size)]
        self.people = []
        self.exit = (random.randint(0, size-1), random.randint(0, size-1))
        self.grid[self.exit[0]][self.exit[1]] = EXIT

        for i in range(num_people):
            while True:
                x, y = random.randint(0, size-1), random.randint(0, size-1)
                if self.grid[x][y] == EMPTY:
                    self.grid[x][y] = PERSON
                    self.people.append(Person(f'P{i}', (x, y)))
                    break

    def print_maze(self):
        for row in self.grid:
            print(' '.join(row))
        print()

    def is_valid(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def bfs(self, start):
        visited = set()
        queue = deque([(start, [])])
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == self.exit:
                return path + [(x, y)]
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny) and (nx, ny) not in visited:
                    if self.grid[nx][ny] != BLOCK:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), path + [(x, y)]))
        return None

    def place_element(self, symbol):
        x, y = map(int, input(f"Ingresa coordenadas para {symbol} (x y): ").split())
        if self.grid[x][y] == EMPTY:
            self.grid[x][y] = symbol

    def next_iteration(self):
        for person in self.people:
            if person.skip_turn:
                print(f"{person.name} pierde turno por retrasador.")
                person.skip_turn = False
                continue

            path = self.bfs(person.pos)
            if not path:
                print(f"{person.name}: ay muchachos...")
                continue

            next_pos = path[1] if len(path) > 1 else path[0]
            dx, dy = next_pos[0] - person.pos[0], next_pos[1] - person.pos[1]
            if (dx, dy) in person.disabled_dirs:
                print(f"{person.name} no puede moverse en esa dirección.")
                continue

            # Actualizar posición
            x, y = person.pos
            self.grid[x][y] = EMPTY
            px, py = next_pos
            person.pos = next_pos
            self.grid[px][py] = PERSON

            # Guardar decisión en árbol histórico
            self._add_to_history(person.history_tree, person.pos)

            # Revisar efectos
            if self.grid[px][py] == TRAP:
                person.disabled_dirs.append(random.choice(DIRECTIONS))
                print(f"{person.name} cayó en trampa.")
            elif self.grid[px][py] == DELAY:
                person.skip_turn = True
                print(f"{person.name} fue retrasado.")

    def _add_to_history(self, node, pos):
        for child in node['children']:
            if child['pos'] == pos:
                return
        node['children'].append({'pos': pos, 'children': []})

    def run(self):
        while True:
            print("""
1. Iniciar simulación
2. Colocar bloqueos
3. Colocar trampas
4. Colocar retrasadores
5. Visualizar estado
6. Ejecutar siguiente iteración
7. Salir
""")
            choice = input("Opción: ")
            if choice == '2': self.place_element(BLOCK)
            elif choice == '3': self.place_element(TRAP)
            elif choice == '4': self.place_element(DELAY)
            elif choice == '5': self.print_maze()
            elif choice == '6': self.next_iteration()
            elif choice == '7': break
            elif choice == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_maze()


# Ejecutar
if __name__ == "__main__":
    maze = Maze(size=8, num_people=2)
    maze.run()
