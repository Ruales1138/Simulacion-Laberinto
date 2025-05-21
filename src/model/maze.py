import sys
sys.path.append('src')
from model.tree import GeneralTree
import random


class Maze:
    def __init__(self, n_casillas, n_jugadores):
        self.arbol = GeneralTree()
        self.vacio: str = '  '
        self.bloqueo: str = '🧱'
        self.jugador: str = '👶'
        self.meta: str = '🚩'
        self.recorrido: str = '🔷'
        self.trampa: str = '💀'
        self.n_casillas: int = n_casillas
        self.n_jugadores: int = n_jugadores
        self.laberinto = None
        self.ubicacion_jugadores = []
        self.ubicacion_meta = None
        self.direcciones_bloqueadas = {'arriba': False, 'abajo': False, 'isquierda': False, 'derecha': False}
        self.crear_laberinto()
    
    def generar_matriz(self, fila: int = 0, columna: int = 0, matriz: list[list[int]] = [], fila_completa: list[int] = []) -> list[list[int]]:
        if fila == self.n_casillas:
            return matriz
        if columna == self.n_casillas:
            matriz.append(fila_completa)
            return self.generar_matriz(fila+1, 0, matriz, [])
        fila_completa.append(random.choice([self.bloqueo, self.vacio, self.vacio, self.vacio]))
        return self.generar_matriz(fila, columna+1, matriz, fila_completa)
    
    def ubicar_aleatorio(self, elemento):
        x = random.randint(0, self.n_casillas-1)
        y = random.randint(0, self.n_casillas-1)
        if self.laberinto[x][y] != self.jugador:
            self.laberinto[x][y] = elemento
            return x, y
        else:
            return self.ubicar_aleatorio(elemento)

    def crear_jugadores(self):
        for _ in range(self.n_jugadores):
            x, y = self.ubicar_aleatorio(self.jugador)
            self.ubicacion_jugadores.append((x, y))

    def crear_meta(self):
        x, y = self.ubicar_aleatorio(self.meta)
        self.ubicacion_meta = (x, y)

    def crear_laberinto(self):
        self.laberinto = self.generar_matriz()
        self.crear_jugadores()
        self.crear_meta()

    def retornar_laberinto(self):
        return self.laberinto
    
    def crear_arbol_DFS(self, current = None, casillas_visitadas = []):
        if current is None:
            current = self.ubicacion_jugadores[0]
            casillas_visitadas.append(current)
        x = current[0]
        y = current[1]

        if x+1 < self.n_casillas and self.laberinto[x+1][y] != self.bloqueo:
            nueva_ubicacion = (x+1, y)
            if nueva_ubicacion not in casillas_visitadas:
                casillas_visitadas.append(nueva_ubicacion)
                self.arbol.insert(current, nueva_ubicacion)
                self.crear_arbol_DFS(nueva_ubicacion, casillas_visitadas)

        if x-1 >= 0 and self.laberinto[x-1][y] != self.bloqueo:
            nueva_ubicacion = (x-1, y)
            if nueva_ubicacion not in casillas_visitadas:
                casillas_visitadas.append(nueva_ubicacion)
                self.arbol.insert(current, nueva_ubicacion)
                self.crear_arbol_DFS(nueva_ubicacion, casillas_visitadas)

        if y+1 < self.n_casillas and self.laberinto[x][y+1] != self.bloqueo:
            nueva_ubicacion = (x, y+1)
            if nueva_ubicacion not in casillas_visitadas:
                casillas_visitadas.append(nueva_ubicacion)
                self.arbol.insert(current, nueva_ubicacion)
                self.crear_arbol_DFS(nueva_ubicacion, casillas_visitadas)

        if y-1 >= 0 and self.laberinto[x][y-1] != self.bloqueo:
            nueva_ubicacion = (x, y-1)
            if nueva_ubicacion not in casillas_visitadas:
                casillas_visitadas.append(nueva_ubicacion)
                self.arbol.insert(current, nueva_ubicacion)
                self.crear_arbol_DFS(nueva_ubicacion, casillas_visitadas)

    def crear_arbol_BFS(self):
        self.arbol.delete_tree() 
        inicio = self.ubicacion_jugadores[0]
        fila = [inicio]
        casillas_visitadas = []
        while fila:
            current = fila.pop()
            x = current[0]
            y = current[1]

            if (
                self.direcciones_bloqueadas['abajo'] is False and 
                x+1 < self.n_casillas and 
                self.laberinto[x+1][y] != self.bloqueo and 
                self.laberinto[x+1][y] != self.recorrido
                ):
                nueva_ubicacion = (x+1, y)
                if nueva_ubicacion not in casillas_visitadas:
                    casillas_visitadas.append(nueva_ubicacion)
                    self.arbol.insert(current, nueva_ubicacion)
                    fila.append(nueva_ubicacion)

            if (
                self.direcciones_bloqueadas['arriba'] is False and
                x-1 >= 0 and 
                self.laberinto[x-1][y] != self.bloqueo and 
                self.laberinto[x-1][y] != self.recorrido
                ):
                nueva_ubicacion = (x-1, y)
                if nueva_ubicacion not in casillas_visitadas:
                    casillas_visitadas.append(nueva_ubicacion)
                    self.arbol.insert(current, nueva_ubicacion)
                    fila.append(nueva_ubicacion)

            if (
                self.direcciones_bloqueadas['derecha'] is False and 
                y+1 < self.n_casillas and 
                self.laberinto[x][y+1] != self.bloqueo and 
                self.laberinto[x][y+1] != self.recorrido
                ):
                nueva_ubicacion = (x, y+1)
                if nueva_ubicacion not in casillas_visitadas:
                    casillas_visitadas.append(nueva_ubicacion)
                    self.arbol.insert(current, nueva_ubicacion)
                    fila.append(nueva_ubicacion)

            if (
                self.direcciones_bloqueadas['isquierda'] is False and 
                y-1 >= 0 and 
                self.laberinto[x][y-1] != self.bloqueo and 
                self.laberinto[x][y-1] != self.recorrido
                ):
                nueva_ubicacion = (x, y-1)
                if nueva_ubicacion not in casillas_visitadas:
                    casillas_visitadas.append(nueva_ubicacion)
                    self.arbol.insert(current, nueva_ubicacion)
                    fila.append(nueva_ubicacion)

    def imprimir_arbol(self):
        self.arbol.print()

    def definir_ruta(self):
        ruta = self.arbol.BFS(self.ubicacion_meta)
        return ruta
    
    def simular_ruta(self):
        self.crear_arbol_BFS()
        self.imprimir_arbol()
        return self.definir_ruta()
    
    def bloqueo_aleatorio(self):
        x = random.randint(0, len(self.laberinto) - 1)
        y = random.randint(0, len(self.laberinto) - 1)
        if self.laberinto[x][y] == self.vacio:
            self.laberinto[x][y] = self.bloqueo
        else:
            self.bloqueo_aleatorio()

    def trampa_aleatoria(self):
        x = random.randint(0, len(self.laberinto) - 1)
        y = random.randint(0, len(self.laberinto) - 1)
        if self.laberinto[x][y] == self.vacio:
            self.laberinto[x][y] = self.trampa
        else:
            self.trampa_aleatoria()

    def ejecutar_trampa(self):
        direccion = random.randint(0, 3)
        if direccion == 0:
            self.direcciones_bloqueadas['arriba'] = True
            print('\n💀 Direccion hacia arriba bloqueada 💀')
        if direccion == 1:
            self.direcciones_bloqueadas['abajo'] = True
            print('\n💀 Direccion hacia abajo bloqueada 💀')
        if direccion == 2:
            self.direcciones_bloqueadas['isquierda'] = True
            print('\n💀 Direccion hacia la isquierda bloqueada 💀')
        if direccion == 3:
            self.direcciones_bloqueadas['derecha'] = True
            print('\n💀 Direccion hacia la derecha bloqueada 💀')
    
    def siguiente_iteracion(self):
        ruta = self.definir_ruta()
        if len(ruta) < 2:
            return False
        else:
            posicion = self.ubicacion_jugadores[0]
            x = posicion[0]
            y = posicion[1]
            self.laberinto[x][y] = self.recorrido
            nueva_pos = ruta[1].value
            nx = nueva_pos[0]
            ny = nueva_pos[1]
            if self.laberinto[nx][ny] == self.trampa:
                self.ejecutar_trampa()
            self.laberinto[nx][ny] = self.jugador
            self.ubicacion_jugadores[0] = nueva_pos
            self.bloqueo_aleatorio()
            self.trampa_aleatoria()
            if self.ubicacion_jugadores[0] == self.ubicacion_meta:
                return True
            





    

