# 🌳 The Maze of Terror 🌀
## 🎯 Contexto del Juego
Un grupo de M personas está atrapado en un laberinto dinámico de tamaño NxN. Existe
solo una salida, ubicada aleatoriamente en la matriz.


Cada persona intentará escapar, pero el laberinto colocará dinámicamente bloqueos,
trampas y retrasadores, dificultando su objetivo de sobrevivir.
## 🕹 Reglas del Juego
- Inicialmente, cada persona se ubica en una posición aleatoria de la matriz.
- En cada iteración:
  - Cada persona calcula la ruta más corta hacia la salida, utilizando estructuras tipo árbol.
  - Las personas solo se mueven una celda por iteración, incluyendo diagonales si están disponibles.
- Cada iteración, el laberinto atacará colocando de manera aleatoria bloqueos, trampas o retrasadores.
## 📌 Efectos de Elementos en el Laberinto
-  Bloqueos (muros):
  - Impiden totalmente el paso y se consideran celdas bloqueadas en el cálculo de ruta.
- Trampas:
  - Al activarse, hacen que la persona afectada pierda permanentemente una dirección aleatoria de movimiento (arriba, abajo, izquierda, derecha o diagonales).
  - Las trampas no bloquean la celda para el cálculo de ruta.
- Retrasadores:
○ Al activarse, hacen que la persona pierda un turno.
○ Tampoco bloquean la celda para el cálculo de ruta.
Si la ruta hacia la salida deja de existir debido a bloqueos, el personaje declara "ay
muchachos..." y deja de moverse, aceptando su destino.
🎨 Visualización
Es clave que en cada iteración, por cada persona:
● Se visualice claramente el laberinto en consola o interfaz gráfica.
● Se destaque en un color llamativo la ruta completa desde la posición actual de
cada persona hasta la salida.
● Los elementos del laberinto deben distinguirse claramente:
○ Personas: caracteres o iconos específicos.
○ Salida: un símbolo claro (ej: 🏁).
○ Bloqueos: celdas rellenas en negro o símbolos tipo "X".
○ Trampas: símbolos diferentes, como "T".
○ Retrasadores: símbolos diferentes, como "R".
Recuerda:
● Solo los bloqueos afectan el cálculo de la ruta más corta.
● Las trampas y retrasadores se deben ver claramente en el mapa pero no afectan la
elección de ruta.
📋 Menú Interactivo
La aplicación deberá contar con un menú que permita al usuario:
1. Iniciar simulación: comienza el juego con posiciones aleatorias de salida y
personajes.
2. Colocar bloqueos: permitir al usuario definir posiciones arbitrarias para nuevos
bloqueos.
3. Colocar trampas: permitir al usuario definir posiciones arbitrarias para nuevas
trampas.
4. Colocar retrasadores: permitir al usuario definir posiciones arbitrarias para nuevos
retrasadores.
5. Visualizar estado actual del laberinto.
6. Ejecutar siguiente iteración: recalcula rutas y actualiza posiciones.
7. Salir del juego.
⚙️ Estructuras Técnicas Requeridas
● Árbol de Rutas:
○ Representar la ruta más corta calculada en cada iteración mediante árboles
(BFS o Dijkstra).
● Árbol Histórico de Decisiones:
○ Cada persona deberá mantener un registro en forma de árbol que registre
todas las decisiones tomadas en cada iteración:
■ Nodo raíz: posición inicial del personaje.
■ Cada nodo: celda visitada con información sobre la iteración y
dirección elegida.
■ Ramas: representan decisiones alternativas disponibles desde cada
celda.
○ Este árbol permitirá analizar posteriormente la lógica detrás de cada decisión
tomada por los personajes.
○ Ejemplo Gráfico:
Persona A - Inicio (Celda 2,2)
── Iteración 1: Celda 3,3 (decisión elegida)
│ ├── Iteración 2: Celda 4,4 (decisión elegida)
│ │ ├── Iteración 3: Celda 5,5 (Salida 🏁)
│ │ └── Iteración 3: Celda 4,5 (alternativa no elegida)
│ └── Iteración 2: Celda 3,4 (alternativa no elegida)
└── Iteración 1: Celda 2,3 (alternativa no elegida)
🌟 Mejoras adicionales (opcionales)
Para obtener bonificaciones, considera:
● Personajes con habilidades especiales.
● Eventos especiales (derrumbes, inundaciones, explosiones).
● Interacción entre personajes (compartir información, ayudar a recuperar
movimientos).
📈 Criterios de evaluación - Implementación (40%)
Aspecto Peso
Modelado eficiente del laberinto dinámico y personajes y buenas
prácticas de programación.
20%
Uso adecuado de estructuras de árboles para rutas y daños 30%
Implementación eficiente de algoritmos de búsqueda 30%
Representación visual clara y dinámica de rutas e iteraciones 20%
Implementación de mejoras adicionales +10%
📈 Criterios de evaluación - Sustentación Práctica
(60%)
Fecha de entrega
Grupo 61: 22 de mayo
Grupo 62: 23 de mayo
Grupo 63: 22 de mayo
Grupo 64: 23 de mayo
