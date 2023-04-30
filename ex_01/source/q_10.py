import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
edges = [('A', 'B', 1), ('A', 'G', 2), ('B', 'C', 2), ('B', 'D', 2), ('C', 'B', 2), ('C', 'D', 1), ('D', 'B', 2), ('D', 'E', 1), ('D', 'F', 1), ('D', 'G', 2), ('D', 'H', 1), ('G', 'A', 2), ('G', 'D', 2)]
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

nx.draw(G, with_labels=True)
plt.show()