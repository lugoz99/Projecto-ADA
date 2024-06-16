import random
import math

COOLING_RATE = 0.99


def linear_search_simulated_annealing(prob_table, target, temperature, st):
    """
    Realiza una búsqueda lineal con recocido simulado en la tabla de probabilidad.
    
    Args:
    - prob_table (list): La tabla de probabilidad a explorar.
    - target (int): El valor objetivo a buscar.
    - temperature (float): La temperatura inicial para el recocido simulado.
    - present_state (tuple): El estado presente (fila, columna) en la tabla.
    - future_state (tuple): El estado futuro (fila, columna) en la tabla.
    
    Returns:
    - result (tuple): La posición (fila, columna) donde se encontró el objetivo, o None si no se encontró.
    - steps (list): Lista de todos los estados evaluados durante la búsqueda.
    """
    n = len(prob_table)
    steps = []
    
    # Comenzar desde el estado presente
    i, j = present_state
    
    # Buscar en la tabla de probabilidad
    while i < n and j < n:
        current_value = prob_table[i][j]
        steps.append((i, j, current_value))
        
        # Verificar si se ha encontrado el objetivo
        if current_value == target:
            return (i, j), steps
        
        # Mover al estado futuro
        i, j = future_state
        
        # Aplicar recocido simulado para decidir si aceptar el movimiento
        if accept_move(current_value, target, temperature):
            return (i, j), steps
        
        # Reducir la temperatura
        temperature = cool_down(temperature)
    
    return None, steps

def accept_move(current_value, target, temperature):
    """
    Decide si aceptar un movimiento basado en la diferencia de valor y la temperatura.
    
    Args:
    - current_value (int): El valor actual en la tabla de probabilidad.
    - target (int): El valor objetivo a buscar.
    - temperature (float): La temperatura actual para el recocido simulado.
    
    Returns:
    - bool: True si se acepta el movimiento, False de lo contrario.
    """
    if current_value == target:
        return True
    else:
        return random.random() < math.exp(-abs(current_value - target) / temperature)

def cool_down(temperature):
    """
    Reduce la temperatura conforme avanza la búsqueda.
    
    Args:
    - temperature (float): La temperatura actual para el recocido simulado.
    
    Returns:
    - float: La temperatura reducida.
    """
    return temperature * COOLING_RATE

