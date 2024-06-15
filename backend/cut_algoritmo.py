import matplotlib.pyplot as plt
from scipy.stats import wasserstein_distance
import numpy as np
import networkx as nx
from chartPlotter.ProbabilityTransitionController import (
    probabilityTransitionTable,
    graphProbability,
)
from backend.auxiliares import (
    repr_current_to_array,
    repr_next_to_array,
    ordenar_matriz_product,
    build_probabilities,
)


def dfs(G, node, visited, end_node):
    visited.add(node)
    for neighbor in G.neighbors(node):
        if neighbor not in visited:
            dfs(G, neighbor, visited, end_node)

        if end_node in visited:
            return


def is_bipartite(G, start_node, end_node):
    visited = set()
    dfs(G, start_node, visited, end_node)

    return end_node not in visited


def cut_process(ns, cs, cs_value, probabilities, states ,st):
    G = nx.DiGraph()
    add_connections(G, ns, cs)
    st.write("Grafo principal")
    draw_graph(G,st)

    nodes = list(G.nodes())
    start_node = nodes[0]
    if is_bipartite(G, start_node, start_node):
        st.info("El grafo ya está particionado, el proceso termina")
        return

    min_partition = {
        "partitioned_system": [],
        "partition": "",
        "edge_to_remove_1": "",
        "edge_to_remove_2": "",
        "emd": 0,
    }

    start_process(G, ns, cs, cs_value, min_partition, probabilities, states,st)

    '''

    edge_to_remove_1 = min_partition["edge_to_remove_1"]
    edge_to_remove_2 = min_partition["edge_to_remove_2"]

    if min_partition["emd"] > 0 and edge_to_remove_1 != "" and edge_to_remove_2 != "":
        G.remove_edge(edge_to_remove_1, edge_to_remove_2)
        G.remove_edge(edge_to_remove_2, edge_to_remove_1)

    st.write("Grafo final")
    draw_graph(G)

    if min_partition["partition"]:
        st.caption("Minima partición")
        st.caption("emd", min_partition["emd"])
        st.caption("partition", min_partition["partition"])
        graphProbability(min_partition["partitioned_system"],st)

    '''


def start_process(G, ns, cs, cs_value, min_partition, probabilities, states, st):
    memory = {}
    probabilities = build_probabilities(probabilities, len(states))
    original_system = probabilityTransitionTable(
        repr_current_to_array(cs, cs_value), repr_next_to_array(ns), probabilities, states
    )

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
            draw_graph(G)

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

                elif emd_distance <= min_partition.get("emd"):
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
        value = probabilityTransitionTable(
            repr_current_to_array(cs, cs_value), repr_next_to_array(ns), probabilities, states
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


def draw_graph(G, st):
    pos = nx.circular_layout(G)
    fig, ax = plt.subplots()
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_size=10,
        font_color="black",
        arrowsize=20,
    )
    st.pyplot(fig)
