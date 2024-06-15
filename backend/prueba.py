# Definimos los conjuntos A y B
conjunto_presente = {"A", "C"}
conjunto_futuro = {"A", "B", "C"}

# Generamos todos los subconjuntos de un conjunto dado
from itertools import chain, combinations


def obtener_subconjuntos(conjunto):
    """Devuelve todos los subconjuntos de un conjunto dado."""
    s = list(conjunto)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


# Obtenemos todos los subconjuntos de ambos conjuntos
subconjuntos_presente = obtener_subconjuntos(conjunto_presente)
subconjuntos_futuro = obtener_subconjuntos(conjunto_futuro)

# Generamos todas las combinaciones de subconjuntos de ambos conjuntos
todos_subconjuntos_combinados = [
    (sp, sf) for sp in subconjuntos_presente for sf in subconjuntos_futuro
]


# for sp, sf in todos_subconjuntos_combinados:
#     print(f"futuro: {sf}, presente: {sp}")


# Para cada tupla en la lista, imprimir la combinación original y luego cada elemento en el conjunto futuro dado el conjunto presente
for tupla in todos_subconjuntos_combinados:
    futuro, presente = tupla
    print(f"Original: futuro: {futuro}, presente: {presente}")
    for elemento in futuro:
        print(f"P({elemento}|{presente})")
