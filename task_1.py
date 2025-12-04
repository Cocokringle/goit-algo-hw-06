import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

cities = ["Київ", "Чернівці", "Полтава", "Харків", "Івано-Франківськ", "Севастополь"]
G.add_nodes_from(cities)

G.add_edge("Київ", "Харків", weight=480)
G.add_edge("Полтава", "Харків", weight=145)
G.add_edge("Київ", "Івано-Франківськ", weight=600)
G.add_edge("Київ", "Севастополь", weight=900)
G.add_edge("Івано-Франківськ", "Чернівці", weight=135)
G.add_edge("Київ", "Полтава", weight=340)

options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True,
    "arrows": True
}

# print(G.nodes())
# print(G.edges())

degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# print(degree_centrality)
# print(closeness_centrality)
# print(betweenness_centrality)

nx.draw(G, **options)
plt.show()