import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
diG = nx.DiGraph()
nodes = [1, 2, 3, 4, 5, 6]
edges = [(2, 5), (6, 1), (5, 3), (2, 3)]

G.add_nodes_from(nodes)
G.add_edges_from(edges)
diG.add_nodes_from(nodes)
diG.add_edges_from(edges)

nx.draw(G, with_labels=True)
nx.draw(diG, with_labels=True)
plt.show()
