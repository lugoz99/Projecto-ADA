import os
import sys

# Obtener la ruta del directorio raíz del proyecto
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(ROOT_DIR)

# Agregar el directorio raíz al sys.path
sys.path.append(PARENT_DIR)
import pytest


from backend.Algorithms.GrafoBipartito import GrafoBipartito


def create_non_bipartite_graph():
    grafo = GrafoBipartito()

    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")

    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("D", "A")
    grafo.agregar_arista("A", "C")

    return grafo


def create_bipartite_graph():
    grafo = GrafoBipartito()
    grafo.agregar_vertice("A")
    grafo.agregar_vertice("B")
    grafo.agregar_vertice("C")
    grafo.agregar_vertice("D")
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("B", "C")
    grafo.agregar_arista("C", "D")
    grafo.agregar_arista("D", "A")
    return grafo


def test_bipartite_true():
    bipartite_graph = create_bipartite_graph()

    assert bipartite_graph.es_bipartito() == True


def test_bipartite_false():
    non_bipartite_graph = create_non_bipartite_graph()
    assert non_bipartite_graph.es_bipartito() == False


if __name__ == "__main__":
    pytest.main()
