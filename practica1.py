import networkx as nx
import graphviz

G = nx.Graph()

# Agregamos los nodos; n nodos

G.add_node('V')
G.add_node('R')
G.add_node('A')
G.add_node('AM')

#agregamos las ramas; a que nodo va el nodo

G.add_edge('V', 'R')
G.add_edges_from([('A', 'AM'), ('R', 'AM')])

#Agregamos los atributos a nodos y las aristas

G.nodes['V']['colorNode'] = 'verde'

# G.edges['V', 'R']['colorN'] = 'rama1'

print(G.nodes(data=True))
print(G.nodes['V'])

#Generamos la salida
A = nx.nx_agraph.to_agraph(G)
A.layout('dot')
# A.draw('salida2.png')

# print(G.nodes)