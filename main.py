

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

nodelist = pd.read_csv('nodosList.csv',delimiter=";")
edgelist = pd.read_csv('aristasList.csv',delimiter=";")


g = nx.Graph()

for i, edgeRow in edgelist.iterrows():
    g.add_edge(edgeRow[0], edgeRow[1], attr_dict=edgeRow[2:].to_dict())

for i, nodeRow in nodelist.iterrows():
    g.add_node(nodeRow[0], attr_dict=nodeRow[1:].to_dict())


node_positions = dict()
for node in g.nodes(data=True):
    node_positions[node[0]] = (node[1]['attr_dict']['X'], node[1]['attr_dict']['Y'])

labels_dict = dict()
for node in g.nodes(data=True):
     labels_dict[node[0]] = node[1]['attr_dict']['LABEL']

edge_distance = list()
for edge in g.edges(data=True):
    edge_distance.append(edge[2]['attr_dict']['distance'])

#print(node_positions)
#print(edge_distance)
print('# of edges: {}'.format(g.number_of_edges()))
print('# of nodes: {}'.format(g.number_of_nodes()))


"""
g.add_nodes_from(
    [
        ("A",{"label":"A"}),
        ("B",{"label":"B"}),
        ("C",{"label":"C"}),
        ("D",{"label":"D"}),
    ]
)
g.add_edges_from(
    [
        ("A","B",{"weight":3.16}),
        ("A","C",{"weight":1}),
        ("A","D",{"weight":3.16}),
    ]
)
"""

"""
BtoD = nx.shortest_path_length(g,source="B",target="D",weight="weight")
print(BtoD)
"""

plt.title('Graph Representation of NIGGA', size=15)
nx.draw(g, pos=node_positions, edge_color="red", node_size=10, node_color='black', with_labels=False)
nx.draw_networkx_labels(g,pos=node_positions,labels=labels_dict,horizontalalignment="left",verticalalignment="top",font_size=10,font_color="black")
plt.show()


