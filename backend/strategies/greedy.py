
import networkx as nx
import matplotlib.pyplot as plt

def greedy_bipartite_v1(prob_table, st):
    U, V = set(), set()
    for i in range(len(prob_table)):
        for j in range(len(prob_table[i])):
            if i != j:
                if prob_table[i][j] > prob_table[j][i]:
                    if i not in U and i not in V:
                        U.add(i)
                    if j not in U and j not in V:
                        V.add(j)
                else:
                    if j not in U and j not in V:
                        U.add(j)
                    if i not in U and i not in V:
                        V.add(i)
    print(U)
    print(V)

    return U, V

def greedy_bipartite(prob_table, st):
    U, V = set(), set()
    steps = []  # Para almacenar los pasos del algoritmo
    G = nx.Graph()  # Grafo para la visualización

    for i in range(len(prob_table)):
        for j in range(len(prob_table[i])):
            if i != j:
                if prob_table[i][j] > prob_table[j][i]:
                    if i not in U and i not in V:
                        U.add(i)
                        G.add_node(i, bipartite=0)  # Añadir nodo al grafo
                    if j not in U and j not in V:
                        V.add(j)
                        G.add_node(j, bipartite=1)  # Añadir nodo al grafo
                    G.add_edge(i, j)  # Añadir arista al grafo
                else:
                    if j not in U and j not in V:
                        U.add(j)
                        G.add_node(j, bipartite=0)  # Añadir nodo al grafo
                    if i not in U and i not in V:
                        V.add(i)
                        G.add_node(i, bipartite=1)  # Añadir nodo al grafo
                    G.add_edge(j, i)  # Añadir arista al grafo
                steps.append((set(U), set(V), list(G.edges)))

    return U, V, steps

def plot_bipartite_process(steps, st):
    for step, (U, V, edges) in enumerate(steps):
        fig, ax = plt.subplots()
        
        B = nx.Graph()
        B.add_nodes_from(U, bipartite=0)
        B.add_nodes_from(V, bipartite=1)
        B.add_edges_from(edges)

        # Posicionamiento automático de los nodos
        pos = nx.spring_layout(B)

        # Dibujo del grafo
        nx.draw(B, pos, with_labels=True, 
                node_color=['lightblue' if node in U else 'lightgreen' for node in B.nodes], 
                edge_color='gray', ax=ax)
        
        plt.title(f'Step {step + 1}')
        
        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
