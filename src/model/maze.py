import sys
sys.path.append('src')
from model.tree import GeneralTree
import random


class Maze:
    def __init__(self, n_casillas, n_jugadores):
        self.n_casillas: int = n_casillas
        self.n_jugadores: int = n_jugadores
        self.laberinto = None
        self.ubicacion_jugadores = []
        self.ubicacion_meta = None
        self.crear_laberinto()
    
    def generar_matriz(self, fila: int = 0, columna: int = 0, matriz: list[list[int]] = [], fila_completa: list[int] = []) -> list[list[int]]:
        if fila == self.n_casillas:
            return matriz
        if columna == self.n_casillas:
            matriz.append(fila_completa)
            return self.generar_matriz(fila+1, 0, matriz, [])
        fila_completa.append(random.choice(['X ', '  ']))
        return self.generar_matriz(fila, columna+1, matriz, fila_completa)
    
    def ubicar_aleatorio(self, elemento):
        x = random.randint(0, self.n_casillas-1)
        y = random.randint(0, self.n_casillas-1)
        if self.laberinto[x][y] != '👶':
            self.laberinto[x][y] = elemento
            return x, y
        else:
            return self.ubicar_aleatorio(elemento)

    def crear_jugadores(self):
        for _ in range(self.n_jugadores):
            x, y = self.ubicar_aleatorio('👶')
            self.ubicacion_jugadores.append((x, y))
        print(self.ubicacion_jugadores)

    def crear_meta(self):
        x, y = self.ubicar_aleatorio('🚩')
        self.ubicacion_meta = (x, y)
        print(self.ubicacion_meta)

    def crear_laberinto(self):
        self.laberinto = self.generar_matriz()
        self.crear_jugadores()
        self.crear_meta()

    def retornar_laberinto(self):
        return self.laberinto
    


m = Maze(5, 10)
laberinto = m.retornar_laberinto()
print(*laberinto, sep="\n")

gt = GeneralTree()
gt.insert((0,0), (2,2))
print(gt)