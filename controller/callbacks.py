from dash import Input, Output, State, no_update, callback_context
import json
from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import os
import dash_cytoscape as cyto
import numpy as np
import pandas as pd


# Callbacks
def register_callbacks(app):

    # Callbacks para la página de personalización en donde se guarda la imagen
    @app.callback(
        Output("network-graph", "generateImage", allow_duplicate=True),
        Input("network-graph", "elements"),
    )
    def update_generate_image(elements):
        return {"type": "png", "action": "store"}

    @app.callback(
        Output("image-data-store", "data"), Input("network-graph", "imageData")
    )
    def store_image_data(imageData):
        return imageData

    # TODO: callback que guarda los datos del formulario [EN USO]
    @app.callback(
        Output("form-data-store", "data"),
        [Input("close", "n_clicks")],
        [
            State("n-nodes-input", "value"),
            State("is-complete-input", "value"),
            State("is-connected-input", "value"),
            State("is-weighted-input", "value"),
            State("is-directed-input", "value"),
        ],
    )
    def store_form_data(
        n_clicks, n_nodes, is_complete, is_connected, is_weighted, is_directed
    ):
        """_summary_

        Args:
            n_clicks (_type_): evento click
            n_nodes (_type_): numero de nodos
            is_complete (bool): grafo completo
            is_connected (bool): grafo conexo
            is_weighted (bool): es ponderado
            is_directed (bool): es dirgido

        Returns:
            _type_: Los datos de formulario aleatorio generado por el usuario
        """
        if not n_clicks:
            return no_update

        form_data = {
            "n_nodes": n_nodes,
            "is_complete": is_complete,
            "is_connected": is_connected,
            "is_weighted": is_weighted,
            "is_directed": is_directed,
        }
        return form_data

    # TODO: AQUI VOY A EDITAR EL CALLBACK PARA QUE GUARDE LOS DATOS DEL FORMULARIO DE EDICION
    @app.callback(
        Output("form-edit-store", "data"),
        [Input('close-update"', "n_clicks")],
        [
            State("input-label", "value"),
            State("input-value", "value"),
            State("input-color", "value"),
        ],
    )
    def store_form_edit(n_clicks, label, valor, color):
        if not n_clicks:
            return no_update

        form_data = {
            "label": label,
            "value": valor,
            "color": color,
        }
        return form_data

    # TODO:Callback para la generancion de una imagen de tipo png y jpg
    @app.callback(
        Output("network-graph", "generateImage"),
        [
            Input("btn-get-jpg", "n_clicks"),
            Input("btn-get-png", "n_clicks"),
        ],
    )
    def update_output(jpg_clicks, png_clicks):
        ctx = callback_context

        if not ctx.triggered:
            return no_update
        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            image_type = button_id.split("-")[-1]

            return {
                "type": image_type,
                "action": "download",
                "filename": "grafo",
                "options": {"full": True},
            }

    # ********************** Callback para guardar el archivo JSON , Dandole un nombre
    @app.callback(
        Output("download", "data"),
        [Input("guardar-como", "n_clicks")],  # Agregado "save-file-as" como Input
        [
            State("network-graph", "elements"),
            State("input", "value"),
        ],  # Cambiado "rename_file" a "input"
        prevent_initial_call=True,
    )
    def func(save_as_clicks, data, filename):
        if (
            save_as_clicks > 0 and filename is not None and data is not None
        ):  # Cambiado "n_clicks" a "save_as_clicks"
            # Serializar los datos a una cadena JSON
            json_data = json.dumps(data)

            # Guardar el objeto JSON en un archivo en el servidor
            with open(os.path.join(os.getcwd(), "data", filename + ".json"), "w") as f:
                f.write(json_data)

            # Devolver los datos para descargar en el sistema del usuario
            return dcc.send_string(json_data, filename=filename + ".json")
        else:
            print("No se ha seleccionado un archivo para guardar")

    # ****************************************************************
    # ***Callback para descargar la matriz de adyacencia en Excel***

    # This callback function is responsible for generating and downloading an Excel file containing the
    # adjacency matrix of a graph represented by the elements provided in the "network-graph".
    @app.callback(
        Output("download-excel", "data", allow_duplicate=True),
        [Input("btn", "n_clicks"), Input("network-graph", "elements")],
        prevent_initial_call=True,
    )
    def func(n_clicks, elements):
        if n_clicks > 0:
            # Crear dos DataFrames vacíos con los nodos como índices y columnas
            nodes = [str(i) for i in range(len(elements))]
            df_binary = pd.DataFrame(0, index=nodes, columns=nodes)
            df_weights = pd.DataFrame(0, index=nodes, columns=nodes)

            # Iterar sobre las aristas del grafo
            for element in elements:
                if "source" in element["data"] and "target" in element["data"]:
                    # Para cada arista, establecer el valor correspondiente en el DataFrame al peso de la arista
                    df_binary.loc[
                        element["data"]["source"], int(element["data"]["target"])
                    ] = 1
                    df_binary.loc[
                        element["data"]["target"], int(element["data"]["source"])
                    ] = 1
                    df_weights.loc[
                        element["data"]["source"], int(element["data"]["target"])
                    ] = element["data"].get("weight", 0)
                    df_weights.loc[
                        element["data"]["target"], int(element["data"]["source"])
                    ] = element["data"].get("weight", 0)

            # Agregar una columna vacía al principio de cada DataFrame
            # df_binary.insert(0, '', '')
            # df_weights.insert(0, '', '')

            # Agregar el título 'Origen/Destino' en la primera celda superior izquierda
            df_binary.columns = ["Origen/Destino"] + [
                str(i) for i in df_binary.columns[1:]
            ]
            df_weights.columns = ["Origen/Destino"] + [
                str(i) for i in df_weights.columns[1:]
            ]

            # Generar un nombre de archivo automáticamente
            file_path = os.path.join(os.getcwd(), "data", "adjacency_matrix.xlsx")

            # Crear un escritor de Excel y escribir ambos DataFrames en diferentes hojas
            with pd.ExcelWriter(file_path) as writer:
                df_binary.to_excel(writer, sheet_name="Binary", index=False)
                df_weights.to_excel(writer, sheet_name="Weights", index=False)

            # Devolver los datos para que se descarguen en el sistema del usuario
            return dcc.send_file(file_path)

    # * ZONA DE MODAL DEL FORMULARIO

    @app.callback(
        Output("modal", "is_open"),
        [Input("generate-button", "n_clicks"), Input("close", "n_clicks")],
        [State("modal", "is_open")],
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

    @app.callback(
        Output("modal-guardar-como", "is_open"),
        [Input("save-file-as", "n_clicks"), Input("guardar-como", "n_clicks")],
        [State("modal-guardar-como", "is_open")],
    )
    def toggle_modal_guardar_como(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

    # *** Generar tabla de la matriz de adyacencia ***

    @app.callback(
        Output("info-grafo", "children", allow_duplicate=True),
        [Input("id-table", "n_clicks")],
        [State("network-graph", "elements")],
        prevent_initial_call=True,
    )
    def tabla(n_clicks, elements):
        if n_clicks is not None and elements is not None:
            conjunto_arista = [
                item["data"]
                for item in elements
                if "source" in item["data"] and "target" in item["data"]
            ]
            df = pd.DataFrame(conjunto_arista)
            nodes = pd.concat([df["source"], df["target"]]).unique()

            # Crear un mapeo de los nodos a números enteros
            node_mapping = {node: i for i, node in enumerate(nodes)}

            # Aplicar el mapeo a los datos de las aristas
            df["source"] = df["source"].map(node_mapping)
            df["target"] = df["target"].map(node_mapping)

            # Crear la matriz de adyacencia con los nodos mapeados
            adjacency_matrix = pd.DataFrame(
                np.zeros((len(nodes), len(nodes)), dtype=int),
                index=range(len(nodes)),
                columns=range(len(nodes)),
            )

            for _, edge in df.iterrows():
                adjacency_matrix.loc[edge["source"], edge["target"]] = 1
                adjacency_matrix.loc[edge["target"], edge["source"]] = 1

            # Crear la tabla
            table = dash_table.DataTable(
                data=adjacency_matrix.reset_index()
                .rename(columns={"index": ""})
                .to_dict("records"),
                columns=[
                    {"name": str(i), "id": str(i)} if i != "" else {"name": i, "id": i}
                    for i in adjacency_matrix.columns
                ],
                style_table={"height": "300px", "overflowY": "auto"},
                style_cell={
                    "height": "auto",
                    # all three widths are needed
                    "minWidth": "50px",
                    "width": "50px",
                    "maxWidth": "50px",
                    "whiteSpace": "normal",
                    "color": "black",
                },
            )
            title = html.H3("Matriz de Representación")

            if table is not None:
                return html.Div([title, table])

    # *** Callback para mostrar la imagen del grafo en la página de información ***
    @app.callback(
        Output("info-grafo", "children"),
        Input("id-grafica", "n_clicks"),
        State("image-data-store", "data"),
        prevent_initial_call=True,
    )
    def display_page(n_clicks, imageData):
        if n_clicks is not None and imageData is not None:
            card_content = [
                dbc.CardBody(
                    children=[
                        html.H4("Modo Imagen", className="card-title"),
                        html.Div(
                            dbc.CardImg(
                                src=imageData,
                                style={
                                    "width": "100%",
                                    "height": "100%",
                                    "display": "block",
                                    "margin": "auto",
                                    "object-fit": "contain",
                                },
                            ),
                            style={
                                "display": "flex",
                                "justify-content": "center",
                                "align-items": "center",
                            },
                        ),
                    ]
                ),
            ]
            return dbc.Card(card_content, className="w-100 h-100")

    # *** Callback para descargar el grafo en formato JSON ***

    @app.callback(
        Output("download-text", "data", allow_duplicate=True),
        [Input("btn-download-txt", "n_clicks")],
        [State("network-graph", "elements")],
        prevent_initial_call=True,
    )
    def download_graph(n_clicks, elements):
        if n_clicks > 0 and elements is not None:
            # Convertir los elementos del grafo a una cadena JSON
            json_data = json.dumps(elements)

            # Devolver los datos para descargar en el sistema del usuario
            return dcc.send_string(json_data, filename="grafo.json")
