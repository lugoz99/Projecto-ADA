import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from networkx import is_bipartite
from scipy.stats import wasserstein_distance
import numpy as np
import networkx as nx
from backend.auxiliares import (
    build_probabilities,
    repr_next_to_array,
    repr_current_to_array,
    ordenar_matriz_product,
)
from backend.marginalizacion import (
    obtener_tabla_probabilidades,
)


def cut_process(ns, cs, cs_value, probabilities, states):
    G = nx.DiGraph()
    add_connections(G, ns, cs)
    print("Grafo principal")

    nodes = list(G.nodes())
    start_node = nodes[0]
    if is_bipartite(G, start_node, start_node):
        print("El grafo ya está particionado, el proceso termina")
        return

    min_partition = {
        "partitioned_system": [],
        "partition": "",
        "edge_to_remove_1": "",
        "edge_to_remove_2": "",
        "emd": 0,
    }

    start_process(G, ns, cs, cs_value, min_partition, probabilities, states)

    print("**********************************************************")

    edge_to_remove_1 = min_partition["edge_to_remove_1"]
    edge_to_remove_2 = min_partition["edge_to_remove_2"]

    if min_partition["emd"] > 0 and edge_to_remove_1 != "" and edge_to_remove_2 != "":
        G.remove_edge(edge_to_remove_1, edge_to_remove_2)
        G.remove_edge(edge_to_remove_2, edge_to_remove_1)

    print("Grafo final")

    if min_partition["partition"]:
        print("Minima partición")
        print("emd", min_partition["emd"])
        print("partition", min_partition["partition"])
    else:
        print("No se genera biparticion minima")


def start_process(G, ns, cs, cs_value, min_partition, probabilities, states):
    memory = {}
    probabilities = build_probabilities(probabilities, len(states))
    original_system = obtener_tabla_probabilidades(
        repr_current_to_array(cs, cs_value),
        repr_next_to_array(ns),
        probabilities,
        states,
    )
    print("|===========================================================|")
    print("| Original System: ", original_system, "    |")
    print("|===========================================================|\n\n")
    print(original_system)
    for i in range(len(ns)):
        nsN = ns[i] + "ᵗ⁺¹"
        for j in range(len(cs)):

            if ns[i] == cs[j]:
                continue

            csC = cs[j] + "ᵗ"

            print("Variable actual", nsN)
            print("cortando", csC, "de", nsN)

            cs_left_cut = cs[:j]
            cs_right_cut = cs[j + 1 :]
            cs_right_partition = cs_left_cut + cs_right_cut

            partition = f"(∅ᵗ⁺¹ | {csC}ᵗ) y ({ns}ᵗ⁺¹ | {cs_right_partition}ᵗ)"
            print("partition: ", partition)

            G.remove_edge(csC, nsN)
            G.remove_edge(nsN, csC)

            arr1 = np.array(cut("", csC, cs_value, memory, probabilities, states))
            arr2 = np.array(
                cut(ns, cs_right_partition, cs_value, memory, probabilities, states)
            )

            partitioned_system = []

            if len(arr1) > 0 and len(arr2) > 0:
                cross_product = np.kron(arr1, arr2)
                partitioned_system = ordenar_matriz_product(cross_product)
            elif len(arr1) > 0:
                partitioned_system = arr1
            elif len(arr2) > 0:
                partitioned_system = arr2

            # Calcular la Distancia de Wasserstein (EMD)
            emd_distance = wasserstein_distance(original_system, partitioned_system)
            print(f"Earth Mover's Distance: {emd_distance}")
            start_node = csC
            end_node = nsN
            if is_bipartite(G, start_node, end_node):
                print("Bipartición generada")
                if min_partition.get("partition") == "":
                    set_min_partition(
                        min_partition,
                        partition,
                        partitioned_system,
                        emd_distance,
                        csC,
                        nsN,
                    )

                if emd_distance == 0:
                    set_min_partition(
                        min_partition,
                        partition,
                        partitioned_system,
                        emd_distance,
                        csC,
                        nsN,
                    )
                    print("minima partición alcanzada")
                    return

                elif emd_distance < min_partition.get("emd"):
                    set_min_partition(
                        min_partition,
                        partition,
                        partitioned_system,
                        emd_distance,
                        csC,
                        nsN,
                    )
                    print("minima partición actualizada")

                G.add_edge(csC, nsN)
                G.add_edge(nsN, csC)
                print("bipartición restarurada con costo:", emd_distance)
            else:
                print("No bipartición generada")
                if emd_distance > 0:
                    G.add_edge(csC, nsN)
                    G.add_edge(nsN, csC)
                    print("conexión restarurada con costo: ", emd_distance)
                else:
                    print("conexión elimina sin perdida de información")

            print("----------   ********** ------------")


def set_min_partition(
    min_partition,
    partition,
    partitioned_system,
    emd_distance,
    edge_to_remove_1,
    edge_to_remove_2,
):
    min_partition["partition"] = partition
    min_partition["partitioned_system"] = partitioned_system
    min_partition["emd"] = emd_distance
    min_partition["edge_to_remove_1"] = edge_to_remove_1
    min_partition["edge_to_remove_2"] = edge_to_remove_2


def cut(ns, cs, cs_value, memory, probabilities, states):
    if memory.get(cs) is not None and memory.get(cs).get(ns) is not None:
        if any(memory.get(cs).get(ns)):
            return memory.get(cs).get(ns)

    if len(ns) == 1:
        value = obtener_tabla_probabilidades(
            repr_current_to_array(cs, cs_value),
            repr_next_to_array(ns),
            probabilities,
            states,
        )
        return value

    value = []
    for i in range(0, len(ns)):
        if len(value) > 0:
            cross_product = np.kron(
                value, cut(ns[i], cs, cs_value, memory, probabilities, states)
            )
            value = ordenar_matriz_product(cross_product)

        else:
            value = np.array(cut(ns[i], cs, cs_value, memory, probabilities, states))

            if memory.get(cs) == None:
                memory[cs] = {}

            memory[cs][ns[i]] = value

    return value


def add_connections(G, ns, cs):
    for i in range(len(ns)):
        n = ns[i] + "ᵗ⁺¹"

        for j in range(len(cs)):
            if ns[i] == cs[j]:
                continue

            c = cs[j] + "ᵗ"
            G.add_node(n)
            G.add_node(c)
            G.add_edge(c, n)
            G.add_edge(n, c)
