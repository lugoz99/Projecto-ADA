from itertools import combinations, product, chain


def gen_system_partitions(m):
    """
    Genera todas las posibles particiones de sistemas para una matriz dada.

    Args:
        m (list): Una matriz 2D representada como una lista de listas.

    Returns:
        list: Una lista de todas las posibles particiones de sistemas.
    """
    if not all(isinstance(row, list) for row in m):
        raise ValueError("La entrada debe ser una matriz 2D (lista de listas).")

    # Genera todas las combinaciones posibles de elementos para cada fila
    row_combinations = [
        chain.from_iterable((combinations(row, r) for r in range(1, len(row))))
        for row in m
    ]

    # Calcula el producto cartesiano de todas las combinaciones de filas
    system_partitions = [list(partition) for partition in product(*row_combinations)]

    # Agrega la partición vacía al resultado
    system_partitions.append([(), ()])

    return system_partitions


from itertools import combinations as iter_combinations


def calculate_negative_set(m, a, b):
    """
    Calculate the negative set for a given matrix.
    """
    negative_a = set(m[0]).difference(a)
    negative_b = set(m[1]).difference(b)

    return tuple(negative_a), tuple(negative_b)


def cartesian_product(a, b, len_a, len_b, include_negative_set=False, m=None):
    prod = []
    items_pushed = set()

    for i in range(len(a)):
        for j in range(len(b)):
            if len(a[i]) == 1 and str(a[i]) not in items_pushed:
                neg_a, neg_b = calculate_negative_set(m, a[i], tuple())
                prod.append([a[i], tuple(), neg_a, neg_b])
                items_pushed.add(str(a[i]))
            if len(b[j]) == 1 and str(b[j]) not in items_pushed:
                neg_a, neg_b = calculate_negative_set(m, tuple(), b[j])
                prod.append([tuple(), b[j], neg_a, neg_b])
                items_pushed.add(str(b[j]))

            neg_a, neg_b = calculate_negative_set(m, a[i], b[j])
            prod.append([a[i], b[j], neg_a, neg_b])

    return prod


def gen_system_partitions(m):

    all_combinations = [[], []]

    for i, row in enumerate(m):
        for j in range(
            1, len(row)
        ):  # 1 to n-1 because we don't want to include the full or empty row
            for combination in iter_combinations(row, j):
                all_combinations[i].append(combination)

    return cartesian_product(
        *all_combinations,
        len_a=len(m[0]),
        len_b=len(m[1]),
        include_negative_set=True,
        m=m
    )


m = [["A", "B", "C"], ["A", "C"]]
print(gen_system_partitions(m))
print(len(gen_system_partitions(m)))


import itertools

lst1 = ["A(p)", "B(p)", "C(p)"]
lst2 = ["A(f)", "C(f)"]

combined_list = lst1 + lst2


def generate_combinations(lst):
    for r in range(1, len(lst)):  # start from 1 to exclude empty set
        for subset in itertools.combinations(lst, r):
            subset_list = list(subset)
            if len(subset_list) == 1:
                subset_list.append("∅")
            yield (subset_list, [item for item in lst if item not in subset_list])


print("Combinations for combined list:")
for index, combination in enumerate(generate_combinations(combined_list)):
    print(index, combination)
