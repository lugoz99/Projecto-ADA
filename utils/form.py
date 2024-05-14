def get_form_data(form_data):

    if form_data:
        """
         Permite obtener los datos del formulario
        Returns:
            _type_: datos del formulario en formato diccionario
        """
        return (
            form_data.get("n_nodes"),
            form_data.get("is_complete"),
            form_data.get("is_connected"),
            form_data.get("is_weighted"),
            form_data.get("is_directed"),
        )
    return None, None, None, None, None


"""_summary_
    Metodo para obtener el nombre del archivo para ser guardado
"""


def obter_input_guardar_como(input_data):
    # * Obtiene el nombre del archivo para guardar
    """_summary_

    Args:
        input_data (_type_): input_data
        Nombre del archivo

    Returns:
        _type_: input_data
    """
    if input_data:
        return input_data
    return None
