"""def handle_close_button(accept_clicks, form_data, elements, stylesheet):
    # Manejar la acción del botón 'close'
    # ...

def handle_update_button(update_clicks, elements, selected_node, node_label, node_value, color_picker_node, stylesheet):
    # Manejar la acción del botón 'update-button'
    # ...
    
    
def handle_close_button(form_data, elements, stylesheet):
    n_nodes, is_complete, is_connected, is_weighted, is_directed = get_form_data(form_data)
    if n_nodes is not None:
        elements = update_network_personalizado(n_nodes, is_weighted, is_directed, is_connected, is_complete)
        if stylesheet is not None and is_directed:
            for style in stylesheet:
                if style["selector"] == "edge":
                    style["style"]["target-arrow-shape"] = "triangle"
    return elements, stylesheet

def handle_update_button():
    # Aquí iría el código para manejar la acción del botón "update-button"
    pass

# Define otras funciones de manejo...



# Mapea los IDs de los botones a sus funciones correspondientes
button_handlers = {
    "close": handle_close_button,
    "update-button": handle_update_button,
    # ...
}

def update_graph(
    # Argumentos...
):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # Llama a la función de manejo apropiada
    handler = button_handlers.get(button_id)
    if handler:
        return handler(accept_clicks, form_data, file_name, file_contents, add_clicks, delete_clicks, update_clicks, add_edge_click, delete_e_clicks, update_e_clicks, edge_label, line_style, show_arrow, color_picker_value, node_label, node_value, color_picker_node, elements, selected_node, selected_edge, stylesheet)
    else:
        return elements, stylesheet
    
    
    
    
button_handlers = {
    "close": handle_close_button,
    "update-button": handle_update_button,
    # Agrega aquí otras funciones de manejo si las hay...
}

def update_graph(
    edge_label,
    line_style,
    show_arrow,
    color_picker_value,
    node_label,
    node_value,
    color_picker_node,
    elements,
    selected_node,
    selected_edge,
    stylesheet,
):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    handler = button_handlers.get(button_id)
    if handler:
        return handler(form_data, elements, stylesheet)
    else:
        return elements, stylesheet"""

"""
@app.callback(
    Output("info-grafo", "children", allow_duplicate=True),
    [Input("id-bipartito", "n_clicks"),
     Input("id-componentes", "n_clicks"),
     Input("id-eliminar", "n_clicks")],
    State("network-graph", "elements"),
)
def actualizar_info(n1, n2, n3, elements):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'id-bipartito':
        # Aquí iría el código para verificar si el grafo es bipartito
        es_bipartito = verificar_bipartito(elements)
        return f"Es bipartito: {es_bipartito}"

    elif button_id == 'id-componentes':
        # Aquí iría el código para obtener las componentes y la conectividad
        componentes_y_conectividad = obtener_componentes(elements)
        return f"Componentes y conectividad: {componentes_y_conectividad}"

    elif button_id == 'id-eliminar':
        # Aquí iría el código para eliminar aristas y verificar la conectividad
        deleted_edges_tuples = [(edge["data"]["source"], edge["data"]["target"]) for edge in deleted_edges]
        resultado_eliminar_aristas = eliminar_aristas(deleted_edges_tuples, elements)
        return f"Resultado eliminar aristas: {resultado_eliminar_aristas}"

    else:
        return 'No clicks yet'



"""


"""
# Después de crear los conjuntos de nodos y las aristas
for edge in edges:
    source, target = edge
    source_color = None
    target_color = None
    # Encuentra el color de los nodos source y target
    for color, nodes in sets.items():
        if any(node["id"] == source for node in nodes):
            source_color = color
        if any(node["id"] == target for node in nodes):
            target_color = color
    # Si los dos nodos de la arista están en el mismo conjunto, el grafo no es bipartito
    if source_color == target_color:
        return "No es bipartito"

# Si todas las aristas conectan nodos en diferentes conjuntos, el grafo es bipartito
return "Es bipartito"

"""


"""
# Crear diccionarios para elementos y estilos
elements_dict = {element["data"]["id"]: element for element in elements}
style_dict = {style["selector"]: style for style in stylesheet}

# Acceder a un elemento específico
if selected_node["id"] in elements_dict:
    node_element = elements_dict[selected_node["id"]]
    # Operar con node_element

# Acceder a un estilo específico
if "node" in style_dict:
    node_style = style_dict["node"]
    # Operar con node_style
    
    


# Actualizar un elemento específico
if selected_node["id"] in elements_dict:
    elements_dict[selected_node["id"]]["data"]["label"] = node_label
    elements_dict[selected_node["id"]]["data"]["value"] = node_value
    # ... (otras actualizaciones)

# Actualizar un estilo específico
if f'node[id = "{selected_node["id"]}"]' in style_dict:
    style_dict[f'node[id = "{selected_node["id"]}"]']["style"]["background-color"] = color_picker_node["hex"]

# Reconstruir las listas actualizadas
elements = list(elements_dict.values())
stylesheet = list(style_dict.values())




# Actualizar un elemento específico
if selected_node["id"] in elements_dict:
    elements_dict[selected_node["id"]]["data"]["label"] = node_label
    elements_dict[selected_node["id"]]["data"]["value"] = node_value
    # ... (otras actualizaciones)

# Actualizar un estilo específico
if f'node[id = "{selected_node["id"]}"]' in style_dict:
    style_dict[f'node[id = "{selected_node["id"]}"]']["style"]["background-color"] = color_picker_node["hex"]

# Reconstruir las listas actualizadas
elements = list(elements_dict.values())
stylesheet = list(style_dict.values())
"""


"""
import networkx as nx
from networkx import bipartite


class GrafoBipartito:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node, bipartite_attribute):
        self.graph.add_nodes_from(node, bipartite=bipartite_attribute)

    def add_edge(self, node1, node2):
        self.graph.add_edge(node1, node2)

    def is_bipartite(self):
        return nx.is_bipartite(self.graph)

    def components_and_connectedness(self):
        if self.is_bipartite():
            if nx.is_connected(self.graph):
                return "El grafo bipartito es conexo y tiene una sola componente."
            else:
                components = list(nx.connected_components(self.graph))
                components_str = ", ".join([str(c) for c in components])
                return f"El grafo bipartito es disconexo y tiene las siguientes componentes: {components_str}"

        else:
            return "El grafo no es bipartito."

    def remove_edges_check_connectedness(self, edges_to_remove):
        for edge in edges_to_remove:
            self.graph.remove_edge(*edge)

        if nx.is_connected(self.graph):
            return "Después de eliminar las conexiones, el grafo sigue siendo conexo."
        else:
            components = list(nx.connected_components(self.graph))
            components_str = ", ".join([str(c) for c in components])
            return f"Después de eliminar las conexiones, el grafo se vuelve disconexo y tiene las siguientes componentes: {components_str}"

    def print_bipartite_sets(self):
        if self.is_bipartite():
            # Obtiene las componentes conectadas del grafo
            components = nx.connected_components(self.graph)

            # Itera sobre las componentes
            for component in components:
                # Obtiene el subgrafo correspondiente a la componente
                subgraph = self.graph.subgraph(component)

                # Obtiene los dos conjuntos de nodos para el subgrafo
                X, Y = bipartite.sets(subgraph)

                # Imprime los nodos en cada conjunto
                print("Conjunto X:")
                for node in X:
                    print(node)

                print("Conjunto Y:")
                for node in Y:
                    print(node)
        else:
            print("El grafo no es bipartito.")



"""


"""
    # button_handlers = {
#     "close": handle_close_button,
#     "update-button": handle_update_button,
#     "open-file": handle_open_file,
#     "add-node-button": handle_add_node_button,
#     "delete-button": handle_delete_button,
# }
"""
