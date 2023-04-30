import networkx as nx
import matplotlib.pyplot as plt

diG = nx.DiGraph()
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
edges = [('A', 'B'), ('A', 'G'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'D'), ('D', 'B'), ('D', 'E'), ('D', 'F'), ('D', 'G'), ('D', 'H'), ('G', 'A'), ('G', 'D')]
diG.add_nodes_from(nodes)
diG.add_edges_from(edges)

nx.draw(diG, with_labels=True)
plt.show()