import networkx as nx
import matplotlib.pyplot as plt
import time

# Una clase para representar un objeto grafo
class Grafo:

    # Constructor
    def __init__(self):
        self.listaAdyacencia = {}

    # Método para agregar una arista dirigida
    def agregar_arista(self, origen, destino):
        if origen not in self.listaAdyacencia:
            self.listaAdyacencia[origen] = []
        self.listaAdyacencia[origen].append(destino)






# Función para realizar un recorrido DFS en el grafo
def DFS(grafo, v, descubierto, G, pos, aristas_recorridas):
    descubierto.add(v)
    print(v, end=' ## ')  # Imprime el nodo actual

    # Visualizar el grafo durante el recorrido
    visualizar_grafo(G, pos, descubierto, aristas_recorridas)

    for u in grafo.listaAdyacencia.get(v, []):
        if u not in descubierto:
            aristas_recorridas.append((v, u))  # Agregar la arista recorrida
            DFS(grafo, u, descubierto, G, pos, aristas_recorridas)
            # Después de volver, añadimos la arista a la lista para mantenerla roja
           # aristas_recorridas.append((u, v)) //ESTE OCASIONABA QUE EL RECORRIDO SE ESTROPEABA
           # EN CADA ITERACION SE AÑADEN Y LUEGO SE QUITAN LAS ARISTAS DEL RECORRIDO
           #PROVOCANDO QUE SE COLOREARAN DE ROJO Y EN LA SIGUIENTE ITERACION VOLVIERAN A COLOR NEGRO

# Función para visualizar el grafo
def visualizar_grafo(G, pos, descubierto, aristas_recorridas):
    # Colores para los nodos
    node_color = ['lightgreen' if node in descubierto else 'lightblue' for node in G.nodes()]

    # Colores para las aristas
    edge_color = []
    for u, v in G.edges():
        if (u, v) in aristas_recorridas or (v, u) in aristas_recorridas:
            edge_color.append('red')  # Arista en el recorrido
        else:
            edge_color.append('black')  # Arista no en el recorrido

    # Dibuja el grafo
    plt.clf()  # Limpiar la figura antes de redibujar
    nx.draw(G, pos, with_labels=True, node_color=node_color, font_weight='bold', node_size=2000, font_size=10,
            arrows=True, arrowstyle='-|>', arrowsize=20, edge_color=edge_color)

    plt.title("Visualización del Grafo durante el recorrido")
    plt.show(block=False)  # Mostrar sin bloquear el hilo
    plt.pause(1)  # Esperar 1 segundo para visualizar el cambio






if __name__ == '__main__':
    grafo = Grafo()

    # Pedir relaciones entre nodos
    print("Dame las aristas entre los nodos: 'nodo1 nodo2'. Escribe 'f' para salir")
    while True:
        linea = input()
        if linea.lower() == 'f':
            break
        origen, destino = linea.split()
        grafo.agregar_arista(origen, destino)

    # Crear el grafo de networkx una sola vez
    G = nx.DiGraph()  # Crear un grafo dirigido
    for origen, destinos in grafo.listaAdyacencia.items():
        for destino in destinos:
            G.add_edge(origen, destino)

    # Definir la posición de los nodos una sola vez
    pos = nx.spring_layout(G)  # Layout para distribuir los nodos

    # Solicitar al usuario el nodo inicial
    nodo_inicial = input('Introduce el nodo inicial del recorrido: ')

    # Inicializar la lista de aristas recorridas
    aristas_recorridas = []

    # Realizar el DFS desde el nodo inicial
    print(f"\nIniciando DFS desde el nodo '{nodo_inicial}':")
    DFS(grafo, nodo_inicial, set(), G, pos, aristas_recorridas)

    # Visualizar el grafo final
    visualizar_grafo(G, pos, set(grafo.listaAdyacencia.keys()), aristas_recorridas)  # Muestra el grafo final
    plt.show()  # Mantener la ventana abierta al final
