# app.py : Inicio de la aplicación


# Importaciones de librerías
# import copy
# import json
import copy
import random
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from dash.exceptions import PreventUpdate


# *Importaciones de carpetas y funciones
from layouts.navbar import header
from layouts.form_page import modal
from layouts.general_layouts import modal_guardar_como
from layouts.buttons import buttons_nodes, buttons_edges, contenedor_info
from utils.visualization import (
    update_network_personalizado,
    load_json_file,
    generate_id,
)
from utils.form import get_form_data
from utils.config import config_stylesheet, style_container_buttons, style_page_content
from controller.callbacks import register_callbacks

from backend.GrafoBipartito import GrafoBipartito


app = dash.Dash(
    __name__,
    prevent_initial_callbacks="initial_duplicate",
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, "style.css"],
)
# The code is likely registering callbacks for an application named `app`. This means that certain
# functions or pieces of code will be executed when specific events or conditions occur within the
# application.
register_callbacks(app)
cyto.load_extra_layouts()
deleted_edges_tuples = []


app.layout = html.Div(
    [
        modal,
        modal_guardar_como,
        header,
        html.Div(
            style=style_container_buttons,
            # The code snippet is creating a list called `children` with three elements:
            # `buttons_nodes`, `contenedor_info`, and `buttons_edges`.
            children=[buttons_nodes, contenedor_info, buttons_edges],
        ),
        dcc.Store(id="form-data-store"),
        dcc.Store(id="network-elements"),
        dcc.Store(id="form-edit-store"),
        dcc.Store(id="image-data-store"),
        html.Div(
            id="page-content",
            className="d-flex justify-content-center align-items-center",
            style=style_page_content,
            children=[
                cyto.Cytoscape(
                    id="network-graph",
                    layout={"name": "cose"},
                    elements=[],
                    stylesheet=config_stylesheet,
                    style={"width": "100%", "height": "800px"},
                    autoRefreshLayout=True,
                ),
            ],
        ),
    ]
)


@app.callback(
    [Output("network-graph", "elements"), Output("network-graph", "stylesheet")],
    [
        Input("close", "n_clicks"),
        Input("form-data-store", "data"),
        Input("open-file", "contents"),
        Input("open-file", "filename"),
        Input("add-node-button", "n_clicks"),
        Input("delete-button", "n_clicks"),
        Input("update-button", "n_clicks"),
        Input("add-edge-button", "n_clicks"),
        Input("delete-edge-button", "n_clicks"),
        Input("update-edge-button", "n_clicks"),
    ],
    [
        State("edge-label-input", "value"),
        State("line-style-dropdown", "value"),
        State("arrow-checklist", "value"),
        State("color-picker", "value"),
        State("node-label-input", "value"),
        State("node-value-input", "value"),
        State("color-picker-node", "value"),
        State("network-graph", "elements"),
        State("network-graph", "selectedNodeData"),
        State("network-graph", "selectedEdgeData"),
        State("network-graph", "stylesheet"),
    ],
)
def update_graph(
    accept_clicks,
    form_data,
    file_name,
    file_contents,
    # Argumentos para nodos
    add_clicks,
    delete_clicks,
    update_clicks,
    # Argumentos para edges
    add_edge_click,
    delete_e_clicks,
    update_e_clicks,
    edge_label,
    line_style,
    show_arrow,
    color_picker_value,
    node_label,
    node_value,
    color_picker_node,
    # -----------------------
    elements,
    selected_node,
    selected_edge,
    stylesheet,
):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    global deleted_edges_tuples
    if button_id == "close":
        # Generar grafo personalizado y actualizar elementos
        # TODO : Actualizar elementos : color , valor para que los tome en cuenta
        n_nodes, is_complete, is_connected, is_weighted, is_directed = get_form_data(
            form_data
        )
        if n_nodes is not None:
            elements = update_network_personalizado(
                n_nodes, is_weighted, is_directed, is_connected, is_complete
            )
            if stylesheet is not None:
                if is_directed:
                    for style in stylesheet:
                        if style["selector"] == "edge":
                            style["style"]["target-arrow-shape"] = "triangle"

    elif button_id == "update-button" and selected_node:
        selected_node = selected_node[0]
        elements_dict = {element["data"]["id"]: element for element in elements}
        if selected_node["id"] in elements_dict:
            # TODO: Sino actualizo deeria dejar los mismo valores
            elements_dict[selected_node["id"]]["data"]["label"] = node_label
            elements_dict[selected_node["id"]]["data"]["value"] = node_value
            if color_picker_node and "hex" in color_picker_node:
                elements_dict[selected_node["id"]]["data"]["color"] = color_picker_node[
                    "hex"
                ]
            else:
                elements_dict[selected_node["id"]]["data"]["color"] = "#5dade2"
            node_style = {
                "selector": f'node[id = "{selected_node["id"]}"]',
                "style": {
                    "background-color": (
                        color_picker_node["hex"]
                        if color_picker_node and "hex" in color_picker_node
                        else "#ABE2FB"
                    ),
                },
            }
            selected_node_style = {
                "selector": f'node[id = "{selected_node["id"]}"]:selected',
                "style": {
                    "background-color": "#FF4136",  # El color que quieras para cuando el nodo está seleccionado
                },
            }
            # Agregar el nuevo selector a la hoja de estilos
            # Mantén la propiedad 'selected' en los datos del nodo
            elements = list(elements_dict.values())  # Actualizar elementos
            stylesheet.append(node_style)
            stylesheet.append(selected_node_style)

    elif (
        button_id == "open-file" and file_contents is not None and file_name is not None
    ):
        # Aquí puedes procesar y visualizar los datos del archivo
        # Por ejemplo, si estás cargando un archivo JSON:
        v = load_json_file(file_name, file_contents)
        if v is not None:
            elements = v

    elif button_id == "add-node-button" and add_clicks is not None:
        # Añadir un nuevo nodo
        if elements is None:
            elements = []

        node_color = None
        for style in config_stylesheet:
            if style["selector"] == "node":
                node_color = style["style"]["background-color"]
                break
        new_node = {
            "data": {
                "id": generate_id(),
                "label": "Node {}".format(add_clicks),
                "value": str(0),
                "color": node_color,
            },
            "position": {
                "x": random.randint(0, 500),
                "y": random.randint(0, 500),
            },  # Agrega coordenadas aleatorias al nodo
        }
        elements.append(new_node)

    elif (
        button_id == "delete-button"
        and delete_clicks is not None
        and selected_node is not None
    ):

        if elements is not None and selected_node is not None:
            selected_node = selected_node[0]
            # Obtener el primer elemento de selected_node
            # Remover el nodo seleccionado de los elementos
            elements = [
                element
                for element in elements
                if element["data"]["id"] != selected_node["id"]
            ]
    # *******CREAR,EDITAR Y ELIMINAR ARISTAS**********************************************

    elif (
        button_id == "add-edge-button"
        and add_edge_click is not None
        and selected_node is not None
    ):
        # Añadir una nueva arista

        edge_id = generate_id()
        new_edge = {
            "data": {
                "id": edge_id,
                "source": selected_node[0]["id"],
                "target": selected_node[-1]["id"],
                "weight": 0,
            }
        }
        elements.append(new_edge)

    elif (
        button_id == "delete-edge-button"
        and delete_e_clicks is not None
        and selected_edge is not None
        and elements is not None
    ):
        # Eliminar arista
        print("Entramos")
        selected_edge_ids = [
            edge["id"] for edge in selected_edge
        ]  # Obtener los IDs de las aristas seleccionadas

        # Añadir las aristas seleccionadas a la lista de aristas eliminadas
        print(selected_edge_ids)
        deleted_edges_tuples.extend(
            [
                element
                for element in elements
                if element["data"]["id"] in selected_edge_ids
            ]
        )

        # Eliminar las aristas seleccionadas de la lista de elementos
        elements = [
            element
            for element in elements
            if element["data"]["id"] not in selected_edge_ids
        ]

    elif (
        button_id == "update-edge-button"
        # and update_e_clicks is not None
        and selected_edge is not None
    ):
        edge_id = selected_edge[0]["id"]  # Obtener el id de la arista seleccionada
        color_hex = color_picker_value["hex"]
        if selected_edge is not None:
            # Crear un diccionario con los elementos para buscar de manera eficiente
            elements_dict = {element["data"]["id"]: element for element in elements}
            # Ahora puedes buscar y modificar el peso de una arista de manera eficiente

            if edge_id in elements_dict and "source" in elements_dict[edge_id]["data"]:
                elements_dict[edge_id]["data"]["weight"] = edge_label

            edge_style = {
                "selector": f'edge[id = "{edge_id}"]',
                "style": {
                    "line-color": color_hex,
                    "line-style": line_style,
                    "target-arrow-shape": (
                        "triangle" if "show-arrow" in show_arrow else "none"
                    ),
                },
            }
            # Agregar el nuevo selector a la hoja de estilos
            stylesheet.append(edge_style)

    return elements, stylesheet


# @app.callback(
#     Output("info-grafo", "children", allow_duplicate=True),
#     [
#         Input("id-grafica", "n_clicks"),
#         Input("open-file", "contents"),
#         Input("open-file", "filename"),
#         Input("close", "n_clicks"),
#         Input("add-node-button", "n_clicks"),
#         Input("add-edge-button", "n_clicks"),
#     ],
#     prevent_initial_call=True,
# )
# def clear_info_grafo(
#     n1, n2, n3, n4, n7, n6
# ):  # Añade más argumentos aquí si agregas más acciones
#     # Este callback se activará si cualquiera de las acciones se realiza
#     return None


# TODO: AQUI HACEMOS LO DEL TALLER 2
"""
    1.El usuario crea un grafo ya sea manualmente o cargando un archivo.
    2.El usuario presiona un botón para verificar si el grafo es bipartito.
    3.El usuario presiona un botón para verificar si el grafo es conexo 
        Y si es disconexo cuántas componentes tiene.
    4.El usuario presiona un botón para eliminar arista(s) y verificar si el grafo sigue siendo conexo
        O es disconexo y muestra sus componentes.


"""


@app.callback(
    Output("info-grafo", "children", allow_duplicate=True),
    Input("id-bipartito", "n_clicks"),
    Input("id-tipo-grafo-bipartito", "n_clicks"),
    Input("id-eliminadas", "n_clicks"),
    Input("network-graph", "elements"),
)
def verificar_bipartito(n, n1, n2, elements):
    global deleted_edges_tuples
    deleted_edges_tuples = []
    if (n < 1 or n1 < 1 or n2 < 1) and len(elements) == 0:
        raise PreventUpdate

    "# Instancia GrafoBipartito"
    print("ELEMENTS", elements)
    print("***************")
    grafo_bipartito = GrafoBipartito()
    # Agregar vértices
    for element in elements:
        if "id" in element["data"]:
            grafo_bipartito.agregar_vertice(element["data"]["id"])

    # Agregar aristas
    for element in elements:
        if "source" in element["data"] and "target" in element["data"]:
            grafo_bipartito.agregar_arista(
                element["data"]["source"], element["data"]["target"]
            )

    print("a eliminar", deleted_edges_tuples)
    if len(deleted_edges_tuples) > 0:
        aristas_eliminadas = [
            (arista["data"]["source"], arista["data"]["target"])
            for arista in deleted_edges_tuples
        ]

        grafo_bipartito.agregar_aristas_eliminadas(aristas_eliminadas)

    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    es_bipartito = grafo_bipartito.es_bipartito()
    print("Aristas", grafo_bipartito.obtener_aristas())
    if button_id == "id-bipartito":
        return [
            (
                dbc.Alert("El grafo es Bipartito", color="success")
                if es_bipartito
                else dbc.Alert("El grafo no es Bipartito", color="danger")
            )
        ]
    elif button_id == "id-tipo-grafo-bipartito":
        if es_bipartito:
            if grafo_bipartito.es_conexo():
                return dbc.Alert("El grafo es conexo en if 2", color="success")
            else:
                cards = []
                componentes = grafo_bipartito.obtener_componentes()
                id_a_label = {
                    element["data"]["id"]: element["data"]["label"]
                    for element in elements
                    if "label" in element["data"]
                }
                componentes_con_labels = [
                    {id_a_label[nodo] for nodo in componente}
                    for componente in componentes
                ]
                for componente in componentes_con_labels:
                    card_content = dbc.CardBody(
                        [
                            dbc.CardHeader("Componente"),
                            html.Div(
                                ", ".join(sorted(componente)),
                                style={"text-align": "center"},
                            ),
                        ]
                    )
                    card = dbc.Card(
                        card_content,
                        inverse=True,
                        style={
                            "width": "18rem",
                            "background-color": "#0083EB71",
                            "color": "#000000",
                        },
                    )
                    cards.append(card)
                return html.Div(
                    children=[
                        dbc.Alert("El grafo es disconexo", color="danger"),
                        dbc.Row(
                            children=cards, className="mx-1"
                        ),  # Envolver las tarjetas en un dbc.Row
                    ]
                )
        else:
            return dbc.Alert("El grafo no es bipartito", color="danger")
    elif button_id == "id-eliminadas":
        deleted_edges_tuples = [
            (edge["data"]["source"], edge["data"]["target"])
            for edge in deleted_edges_tuples
        ]
        # Crear una copia del grafo y eliminar las aristas
        for source, target in deleted_edges_tuples:
            grafo_bipartito.eliminar_arista(source, target)
        # Verificar si el grafo es disconexo
        if not grafo_bipartito.es_conexo():
            # Obtener las componentes conexas
            componentes = grafo_bipartito.obtener_componentes()
            # Generar y devolver una representación de las componentes
            print("len", len(componentes))
            print(componentes)
            cards = []
            print("ELEMENTS", elements)
            print("VERICES", grafo_bipartito.obtener_vertices())
            id_a_label = {
                element["data"]["id"]: element["data"]["label"]
                for element in elements
                if "label" in element["data"]
            }
            componentes_con_labels = [
                {id_a_label[nodo] for nodo in componente} for componente in componentes
            ]
            for componente in componentes_con_labels:
                print(f"Procesando componente: {componente}")

                card_content = dbc.CardBody(
                    [
                        dbc.CardHeader("Componente"),
                        html.Div(
                            ", ".join(sorted(componente)),
                            style={"text-align": "center"},
                        ),
                    ]
                )
                card = dbc.Card(
                    card_content,
                    inverse=True,
                    style={
                        "width": "18rem",
                        "background-color": "#0083EB71",
                        "color": "#000000",
                    },
                )
                cards.append(card)
            return html.Div(
                children=[
                    dbc.Alert("El grafo es disconexo", color="danger"),
                    dbc.Row(
                        children=cards, className="mx-1"
                    ),  # Envolver las tarjetas en un dbc.Row
                ]
            )
        return dbc.Alert("El grafo es Conexo", color="danger")


if __name__ == "__main__":
    app.run_server(debug=True)
