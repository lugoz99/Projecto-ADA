import networkx as nx


class GrafoBipartito:
    def __init__(self):

        self.vertices = {}
        self.aristas_eliminadas = set()  # Almacena las aristas eliminadas
        self.grafo_nx = nx.Graph()

    def agregar_vertice(self, v):
        self.vertices[v] = []
        self.grafo_nx.add_node(v)

    def agregar_arista(self, u, v):
        self.vertices[u].append(v)
        self.vertices[v].append(u)
        self.grafo_nx.add_edge(u, v)

    def marcar_como_eliminada(self, u, v):
        self.aristas_eliminadas.add((u, v))
        self.aristas_eliminadas.add(
            (v, u)
        )  # Asegura que la arista se marque en ambas direcciones

    def agregar_aristas_eliminadas(self, aristas_eliminadas):
        for u, v in aristas_eliminadas:
            self.agregar_arista(u, v)
            self.marcar_como_eliminada(u, v)

    def es_bipartito(self):
        queue = []
        visited = {v: False for v in self.vertices}
        color = {v: -1 for v in self.vertices}

        def bfs():
            while queue:
                u = queue.pop(0)
                visited[u] = True

                for neighbour in self.vertices[u]:
                    if neighbour == u:
                        return False

                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[u]
                        queue.append(neighbour)
                    elif color[neighbour] == color[u]:
                        return False

            return True

        for v in self.vertices:
            if not visited[v]:
                queue.append(v)
                color[v] = 0
                if bfs() == False:
                    return False

        return True

    """
    This Python function checks if a graph is connected by creating a NetworkX graph object from the
    input graph and then using the is_connected function.
    :return: The function `es_conexo` is returning a boolean value indicating whether the graph is
    connected or not. If the number of edges in the graph is 0, it will return `False`. Otherwise, it
    will return the result of `nx.is_connected(G)`, which checks if the graph `G` is connected and
    returns a boolean value.
    """

    def es_conexo(self):
        return nx.is_connected(self.grafo_nx)

    def obtener_componentes(self):
        """
        The function creates a NetworkX graph from a given graph and returns the connected components of
        the graph.
        :return: A list of connected components in the graph represented by the NetworkX object `G`.
        Each connected component is a set of vertices that are connected to each other in the graph.
        """
        # Crear un objeto NetworkX a partir de tu grafo

        # Si el grafo no tiene aristas, devolver los vértices como componentes individuales
        if self.grafo_nx.number_of_edges() == 0:
            return [[v] for v in self.grafo_nx.nodes()]

        print("QUE ES ESTO", [c for c in nx.connected_components(self.grafo_nx)])
        return [c for c in nx.connected_components(self.grafo_nx)]

    def eliminar_arista(self, u, v):
        """
        The function `eliminar_arista` removes an edge between two vertices `u` and `v` in a graph data
        structure.

        :param u: The parameter `u` in the `eliminar_arista` method likely represents one of the vertices of
        the edge that you want to remove from the graph
        :param v: The parameters `u` and `v` in the `eliminar_arista` method represent the two vertices of
        an edge that you want to remove from the graph. The method checks if both vertices `u` and `v` are
        present in the graph's vertices dictionary and then removes the edge between
        """
        if u in self.vertices and v in self.vertices:
            print("SU", u, v)
            self.vertices[u].remove(v)
            self.vertices[v].remove(u)
            self.grafo_nx.remove_edge(u, v)
        else:
            print("NO ENTRAMOS")

    def obtener_aristas(self):
        aristas = []
        for vertice, vecinos in self.vertices.items():
            for vecino in vecinos:
                # Solo agregar la arista si la arista inversa no está ya en la lista
                if (vecino, vertice) not in aristas:
                    aristas.append((vertice, vecino))
        return aristas

    def obtener_vertices(self):
        vertices = []
        for vertice in self.vertices.keys():
            vertices.append(vertice)
        return vertices
