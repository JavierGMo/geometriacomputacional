import networkx as nx
import graphviz

G = nx.Graph()
#Añadir nodos
G.add_node("Kevin Bacon")
G.add_node("Tom Hanks")
G.add_nodes_from(["Meg Ryan", "Parker Posey", "Lisa Kudrow"])
 
#Añadir aristas
G.add_edge("Kevin Bacon", "Tom Hanks")
G.add_edge("Kevin Bacon", "Meg Ryan")
G.add_edges_from([("Tom Hanks", "Meg Ryan"), ("Tom Hanks", "Parker Posey")])
G.add_edges_from([("Parker Posey", "Meg Ryan"), ("Parker Posey", "Lisa Kudrow")])

print(len(G.nodes))
print(len(G.edges))
print(G.nodes)
print(G.edges)


# asignar atributos a nodos y aristas
G.nodes["Tom Hanks"]["oscars"] = 2
G.edges["Kevin Bacon", "Tom Hanks"]["pelicula"] = "Apolo 13"
G.edges["Kevin Bacon", "Meg Ryan"]["pelicula"] = "En carne viva"
G.edges["Parker Posey", "Meg Ryan"]["pelicula"] = "Algo para recordar"
G.edges["Parker Posey", "Tom Hanks"]["pelicula"] = "Tienes un email"
G.edges["Parker Posey", "Lisa Kudrow"]["pelicula"] = "Esperando la hora"
print(G.nodes(data=True))
print(G.edges(data=True))
print(G["Kevin Bacon"])

A = nx.nx_agraph.to_agraph(G)
A.layout('dot')
A.draw('salida.png') # guardar como png
 
# graphviz.Source(A.to_string())  mostrar en jupyter