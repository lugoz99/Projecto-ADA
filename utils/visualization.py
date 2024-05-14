import io
import random
import itertools
import string
import traceback
import networkx as nx
import base64
import json

from dash.exceptions import PreventUpdate


def create_graph(num_nodes, is_weighted, is_directed, is_connected, is_complete):
    # Crear un grafo vacío
    if not is_directed:
        G = nx.Graph()
    else:
        G = nx.DiGraph()

    # Añadir nodos
    G.add_nodes_from(range(num_nodes))

    # Añadir aristas para hacer el grafo completo, si se seleccionó esa opción
    if is_complete:
        G.add_edges_from(itertools.combinations(range(num_nodes), 2))

    # Añadir aristas para hacer el grafo conexo, si se seleccionó esa opción y el grafo no es completo
    elif is_connected and not is_complete:
        for i in range(1, num_nodes):
            G.add_edge(i - 1, i)

    # Añadir pesos a las aristas, si se seleccionó esa opción
    if is_weighted:
        for u, v in G.edges():
            G.edges[u, v]["weight"] = random.randint(1, 100)

    # Convertir el gráfico de NetworkX a un formato que Cytoscape puede utilizar
    # TODO : COMO ASOCIO VALOR,LABEL
    cyto_elements = [
        {"data": {"id": str(node), "label": str(node)}} for node in G.nodes()
    ]
    #     cyto_elements.extend([
    #     {'data': {'source': str(edge[0]), 'target': str(edge[1]), 'weight': str(G.edges[edge]['weight']) if is_weighted else None, 'label': str(G.edges[edge]['weight']) if is_weighted else None}} for edge in G.edges()
    # ])

    # MAS OPTIMO
    """
        cyto_elements.extend([
    {
        "data": {
            "source": str(edge[0]),
            "target": str(edge[1]),
            "weight": G.edges[edge].get("weight", 0),
            "label": str(G.edges[edge].get("weight", 0)),
        }
    }
    for edge in G.edges()
])
    """
    cyto_elements.extend(
        [
            {
                "data": {
                    "source": str(edge[0]),
                    "target": str(edge[1]),
                    "weight": str(G.edges[edge].get("weight", 0)),
                    "label": str(G.edges[edge].get("weight", 0)),
                }
            }
            for edge in G.edges()
        ]
    )

    return cyto_elements


def update_network():
    # Generar características aleatorias
    num_nodes = random.randint(5, 10)
    is_weighted = random.choice([True, False])
    is_directed = random.choice([True, False])
    is_connected = random.choice([True, False])
    is_complete = random.choice([True, False])

    return create_graph(num_nodes, is_weighted, is_directed, is_connected, is_complete)


def update_network_personalizado(
    num_nodes, is_weighted, is_directed, is_connected, is_complete
):
    return create_graph(num_nodes, is_weighted, is_directed, is_connected, is_complete)


def parse_graph_json(graph_json):
    graph_data = graph_json["graph"][0]["data"]

    # Crea los nodos y aristas para Dash-Cytoscape
    nodes = []
    edges = []

    for node in graph_data:
        node_id = str(node["id"])
        nodes.append({"data": {"id": node_id, "label": node["label"]}})

        for linked_node in node["linkedTo"]:
            edges.append(
                {
                    "data": {
                        "source": node_id,
                        "target": str(linked_node["nodeId"]),
                        "weight": linked_node["weight"],
                    }
                }
            )

    return nodes, edges


def mapear_grafo_otro(data_Json):
    if isinstance(data_Json, dict):
        graph_data = data_Json["graph"][0]["data"]

        # Crea los nodos y aristas para Dash-Cytoscape
        nodes = []
        edges = []

        for node in graph_data:
            node_id = str(node["id"])
            nodes.append({"data": {"id": node_id, "label": node["label"]}})

            for linked_node in node["linkedTo"]:
                edges.append(
                    {
                        "data": {
                            "source": node_id,
                            "target": str(linked_node["nodeId"]),
                            "weight": linked_node["weight"],
                        }
                    }
                )
        return nodes + edges


def mapear_grafo(data_Json):
    if isinstance(data_Json, list):
        # Crea los nodos y aristas para Dash-Cytoscape
        nodes = []
        edges = []

        for item in data_Json:
            if "source" not in item["data"]:  # Es un nodo
                node_id = str(item["data"]["id"])
                nodes.append(
                    {
                        "data": {
                            "id": node_id,
                            "label": item["data"]["label"],
                            "value": item["data"]["value"],
                            "color": item["data"]["color"],
                        },
                        "position": item["position"],
                    }
                )
            else:  # Es una arista
                edges.append(
                    {
                        "data": {
                            "id": str(item["data"]["id"]),
                            "source": str(item["data"]["source"]),
                            "target": str(item["data"]["target"]),
                            "weight": item["data"]["weight"],
                        }
                    }
                )
        return nodes + edges


def map_graph(json_data):
    result = mapear_grafo(json_data)
    if result is not None:
        return result
    else:
        return mapear_grafo_otro(json_data)


def load_json_file(contents, filename):
    """
    The function `load_json_file` reads and processes a JSON file uploaded by the user, decoding its
    contents and mapping the data to a graph structure.

    :param contents: The `contents` parameter in the `load_json_file` function is expected to contain
    the content of a file. It seems like the function is designed to handle base64 encoded content,
    decode it, and then process it as JSON data
    :param filename: The `filename` parameter in the `load_json_file` function is a string that
    represents the name of the file being processed. It is used to determine the type of content and how
    to handle it within the function
    :return: The function `load_json_file` will return the variable `elements`, which contains the
    result of processing the JSON data from the file. If an error occurs during the processing, it will
    return the message 'Hubo un error procesando este archivo.'
    """
    elements = None
    if contents is not None and "," in contents:
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)
        try:
            if "json" in filename:
                # Assume that the user uploaded a JSON file
                str_io = io.StringIO(decoded.decode("utf-8"))
                json_data = json.load(str_io)
                elements = map_graph(json_data)
        except Exception as e:
            print(f"Error: {type(e).__name__}")
            print(f"Description: {e}")
            traceback.print_exc()
            return "Hubo un error procesando este archivo."
        return elements
    else:
        raise PreventUpdate


def generate_id(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
