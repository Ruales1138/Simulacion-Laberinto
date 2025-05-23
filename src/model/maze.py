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
        self.meta_2: str = '🚩'
        self.recorrido: str = '🔷'
        self.trampa: str = '💀'
        self.retrasador: str = '🚫'
        self.n_casillas: int = n_casillas
        self.n_jugadores: int = n_jugadores
        self.turno = 0
        self.laberinto = None
        self.ubicacion_jugadores = []
        self.ubicacion_meta = None
        self.ubicacion_meta_2 = None
        self.direcciones_bloqueadas = {'arriba': False, 'abajo': False, 'isquierda': False, 'derecha': False}
        self.turno_bloqueado = None
        self.crear_laberinto()
    
    def generar_matriz(self, fila: int = 0, columna: int = 0, matriz: list[list[int]] = [], fila_completa: list[int] = []) -> list[list[int]]:
        if fila == self.n_casillas:
            return matriz
        if columna == self.n_casillas:
            matriz.append(fila_completa)
            return self.generar_matriz(fila+1, 0, matriz, [])
        fila_completa.append(random.choice([self.bloqueo, self.vacio]))
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

    def crear_meta_2(self):
        x, y = self.ubicar_aleatorio(self.meta_2)
        self.ubicacion_meta_2 = (x, y)

    def crear_laberinto(self):
        self.laberinto = self.generar_matriz()
        self.crear_jugadores()
        self.crear_meta()
        self.crear_meta_2()

    def retornar_laberinto(self):
        return self.laberinto

    def crear_arbol_BFS(self):
        if self.ubicacion_jugadores == []:
            return False
        self.arbol.delete_tree() 
        inicio = self.ubicacion_jugadores[self.turno]
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
                self.laberinto[x+1][y] != self.jugador and 
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
                self.laberinto[x-1][y] != self.jugador and 
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
                self.laberinto[x][y+1] != self.jugador and 
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
                self.laberinto[x][y-1] != self.jugador and 
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
        ruta_2 = self.arbol.BFS(self.ubicacion_meta_2)
        return ruta, ruta_2
    
    def simular_ruta(self):
        respuesta = self.crear_arbol_BFS()
        if respuesta is False:
            return [], []
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

    def retrasador_aleatorio(self):
        x = random.randint(0, len(self.laberinto) - 1)
        y = random.randint(0, len(self.laberinto) - 1)
        if self.laberinto[x][y] == self.vacio:
            self.laberinto[x][y] = self.retrasador
        else:
            self.retrasador_aleatorio()

    def obstaculo_aleatorio(self):
        n_aleatorio = random.randint(0, 2)
        if n_aleatorio == 0:
            self.bloqueo_aleatorio()
        if n_aleatorio == 1:
            self.trampa_aleatoria()
        if n_aleatorio == 2:
            self.retrasador_aleatorio()

    def colocar_boqueo(self, x, y):
        if self.laberinto[x][y] == self.vacio:
            self.laberinto[x][y] = self.bloqueo
            return True
        else:
            return False

    def colocar_trampa(self, x, y):
        if self.laberinto[x][y] == self.vacio:
            self.laberinto[x][y] = self.trampa
            return True
        else:
            return False

    def colocar_retrasador(self, x, y):
        if self.laberinto[x][y] == self.vacio:
            self.laberinto[x][y] = self.retrasador
            return True
        else:
            return False

    def ejecutar_trampa(self):
        direccion = random.randint(0, 3)
        if direccion == 0 and self.direcciones_bloqueadas['arriba'] == False:
            self.direcciones_bloqueadas['arriba'] = True
            print('\n💀 Direccion hacia arriba bloqueada 💀')
            return
        if direccion == 1 and self.direcciones_bloqueadas['abajo'] == False:
            self.direcciones_bloqueadas['abajo'] = True
            print('\n💀 Direccion hacia abajo bloqueada 💀')
            return
        if direccion == 2 and self.direcciones_bloqueadas['isquierda'] == False:
            self.direcciones_bloqueadas['isquierda'] = True
            print('\n💀 Direccion hacia la isquierda bloqueada 💀')
            return
        if direccion == 3 and self.direcciones_bloqueadas['derecha'] == False:
            self.direcciones_bloqueadas['derecha'] = True
            print('\n💀 Direccion hacia la derecha bloqueada 💀')
            return
        self.ejecutar_trampa()

    def ejecutar_retrasador(self):
        self.turno_bloqueado = self.turno
        print(f'\n🚫 Jugador {self.turno + 1} pierde un turno')
    
    def siguiente_iteracion(self):
        ruta, ruta_2 = self.definir_ruta()
        if len(ruta) < 2 and len(ruta_2) < 2:
            self.cambiar_turno()
            return False
        else:
            posicion = self.ubicacion_jugadores[self.turno]
            x = posicion[0]
            y = posicion[1]
            self.laberinto[x][y] = self.recorrido
            nueva_pos = None
            if len(ruta) == 0 and len(ruta_2) > 1:
                nueva_pos = ruta_2[1].value
            if len(ruta_2) == 0 and len(ruta) > 1:
                nueva_pos = ruta[1].value
            if len(ruta) < len(ruta_2) and len(ruta) > 1:
                nueva_pos = ruta[1].value
            if len(ruta_2) < len(ruta) and len(ruta_2) > 1:
                nueva_pos = ruta_2[1].value
            if len(ruta) == len(ruta_2):
                nueva_pos = ruta[1].value
            nx = nueva_pos[0]
            ny = nueva_pos[1]
            if self.laberinto[nx][ny] == self.trampa:
                self.ejecutar_trampa()
            if self.laberinto[nx][ny] == self.retrasador:
                self.ejecutar_retrasador()
            self.laberinto[nx][ny] = self.jugador
            self.ubicacion_jugadores[self.turno] = nueva_pos
            self.obstaculo_aleatorio()
            if self.ubicacion_jugadores[self.turno] == self.ubicacion_meta or self.ubicacion_jugadores[self.turno] == self.ubicacion_meta_2: 
                self.laberinto[nx][ny] = self.meta
                ubicacion = self.ubicacion_jugadores[self.turno]
                self.ubicacion_jugadores.remove(ubicacion)
                self.cambiar_turno()
                return True
            self.cambiar_turno()
            
    def cambiar_turno(self):
        len_j = len(self.ubicacion_jugadores)
        if len_j == 1:
            if self.turno == 0:
                return
            if self.turno == 1:
                self.turno = 0
        else:
            if self.turno + 1 < len_j:
                if self.turno + 1 != self.turno_bloqueado:
                    self.turno += 1
                if self.turno + 1 == self.turno_bloqueado:
                    if self.turno + 2 < len_j:
                        self.turno += 2
                        self.turno_bloqueado = None
                    else:
                        self.turno = 0
                        self.turno_bloqueado = None
            else:
                if 0 != self.turno_bloqueado:
                    self.turno = 0
                else:
                    self.turno = 1
                    self.turno_bloqueado = None

            





    

