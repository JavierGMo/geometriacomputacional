import networkx as nx
import graphviz



def mapNode():
    Gtemp = nx.Graph()

    colorsMap = {
        'verde'   : 0,
        'rojo'    : 0,
        'amarillo': 0,
        'azul'    : 0
    }
    numberNodes = int(input('Numero de nodos: '))
    if numberNodes <= 3:
        raise Exception('El numero de nodos no puede ser menor o igual a 3')
    for color in range(numberNodes):
        print(color)
        Gtemp.add_node(color)
        Gtemp.nodes[color]['colorN'] = color
    print(Gtemp.nodes(data=True))
    #usar un diccionario para saber el numero de nodos que hay

if __name__ == "__main__":
    G = nx.Graph()
    mapNode()

# Agregamos los nodos; n nodos

#G.add_node('V')
#G.add_node('R')
#G.add_node('A')
#G.add_node('AM')

#agregamos las ramas; a que nodo va el nodo
'''
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
'''
