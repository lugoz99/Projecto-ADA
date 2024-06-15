import itertools


def marcar_conjunto_vacio(subconjunto):
    # Reemplazar conjuntos vacíos con el símbolo '∅'
    return subconjunto if len(subconjunto) > 0 else "∅"


def formatear_subconjunto(subconjunto):
    # Convertir tuplas a strings con símbolos específicos
    if subconjunto == "∅":
        return "∅"
    else:
        return "".join(subconjunto)


def generar_biparticiones(conjunto):
    # Generar todas las biparticiones de un conjunto dado
    biparticiones = []
    n = len(conjunto)
    # Recorremos todas las posibles combinaciones de subconjuntos para la mitad del conjunto
    for r in range(n + 1):
        for subset in itertools.combinations(conjunto, r):
            complement = tuple(elem for elem in conjunto if elem not in subset)
            biparticiones.append(
                (marcar_conjunto_vacio(subset), marcar_conjunto_vacio(complement))
            )
    return biparticiones


def generar_combinaciones_biparticiones(ns, cs):
    # Generar todas las biparticiones de ns y cs
    biparticiones_ns = generar_biparticiones(ns)
    biparticiones_cs = generar_biparticiones(cs)

    # Generar todas las combinaciones de las biparticiones de ns y cs
    combinaciones = []
    for ns1, ns2 in biparticiones_ns:
        for cs1, cs2 in biparticiones_cs:
            combinacion_actual = ([ns1, cs1], [ns2, cs2])
            combinaciones.append(combinacion_actual)

    return combinaciones


def formatear_combinaciones(combinaciones):
    # Formatear las combinaciones para que se vean como en la imagen
    combinaciones_formateadas = []
    for (ns1, cs1), (ns2, cs2) in combinaciones:
        combinaciones_formateadas.append(
            [
                (formatear_subconjunto(ns1), formatear_subconjunto(cs1)),
                (formatear_subconjunto(ns2), formatear_subconjunto(cs2)),
            ]
        )
    return combinaciones_formateadas


# Ejemplo de uso
ns = ["A", "B", "C"]
cs = ["A", "C"]


from itertools import product


def calcular_producto_cruz(original_list):
    # Convertir cada elemento de las tuplas en listas individuales
    elementos_0 = [list(t) for t in original_list[0]]
    elementos_1 = [list(t) for t in original_list[1]]

    # Calcular el producto cruz para el elemento 0
    producto_cruz_0 = list(product(elementos_0[0], elementos_0[1]))

    # Calcular el producto cruz para el elemento 1 (si es posible)
    if all(original_list[1]):
        producto_cruz_1 = list(product(elementos_1[0], elementos_1[1]))
    else:
        producto_cruz_1 = None

    return producto_cruz_0, producto_cruz_1


c = generar_combinaciones_biparticiones(ns, cs)
peso = formatear_combinaciones(c)

for idx, element in enumerate(peso):
    producto_cruz_0, producto_cruz_1 = calcular_producto_cruz(element)
    print(idx, element)
    print("Producto cruz del primer conjunto de elementos:", producto_cruz_0)
    print("Producto cruz del segundo conjunto de elementos:", producto_cruz_1)
