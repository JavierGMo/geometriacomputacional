import networkx as nx
import copy
import graphviz
import matplotlib.pyplot as plt


def incrementCounter(var):
    var+=1
    return var

def recursiveAddBranch(objectGraph, node, numberNode,totalNodes):
    if objectGraph == None:
        raise Exception('Not null Graph')
    elif numberNode==totalNodes:
        return objectGraph
    else:
        return recursiveAddBranch(objectGraph, node, numberNode+1, totalNodes)

def mapBranch(objGraph):
    G = objGraph
    Gtemp = copy.deepcopy(G)
    Gnew = nx.Graph()
    
    # print(G.nodes(data=True))
    print(Gtemp.nodes(data=True))

    for graph in Gtemp:
        for tmp in Gtemp:
            # print(Gtemp.nodes[graph]['colorN'])
            if Gtemp.nodes[tmp]['colorN'] != Gtemp.nodes[graph]['colorN']:
                # Gnew.add_edge('{}'.format(graph), '{}'.format(tmp))
                G.add_edge('{}'.format(graph), '{}'.format(tmp))
        # print(Gtemp.nodes[graph])
    print('Node gnew')
    print(Gnew.nodes(data=True))
    return [Gnew, Gtemp]

def mapNode():
    Gtemp = nx.Graph()

    colorsMap = {
        0 : 'verde',
        1 : 'rojo',
        2 : 'amarillo',
        3 : 'azul'
    }
    numberNodes = int(input('Numero de nodos: '))
    countColors = 0
    if numberNodes <= 3:
        raise Exception('El numero de nodos no puede ser menor o igual a 3')
    elif numberNodes == 4:
        # Asignacion de nodos igual a cuatro
        Gtemp.add_node(0)
        Gtemp.nodes[0]['colorN'] = 'verde'
        Gtemp.add_node(1)
        Gtemp.nodes[1]['colorN'] = 'rojo'
        Gtemp.add_node(2)
        Gtemp.nodes[2]['colorN'] = 'amarillo'
        Gtemp.add_node(3)
        Gtemp.nodes[3]['colorN'] = 'azul'
    else:
        # Para numero de nodos mayor a 4
        iterNumber = range(numberNodes)
        for number in iterNumber:
            # print(number)
            Gtemp.add_node(number)
            Gtemp.nodes[number]['colorN'] = colorsMap[countColors]
            print('Count colors: {}, Color : {},iterator {}'.format(countColors, colorsMap[countColors], iterNumber))
            # print(colorsMap[countColors])
            # print(countColors)
            countColors = 0 if (countColors == 3) else incrementCounter(countColors)

    #Asignacion de ramas para cualquier caso mayor igual a 4

    # print(Gtemp.nodes(data=True))
    # print(Gtemp.nodes[0])
    return Gtemp
    #usar un diccionario para saber el numero de nodos que hay

if __name__ == "__main__":
    fig = plt.figure()
    fig.show()
    G = mapNode()
    Gtemp = copy.deepcopy(G)
    GAll = mapBranch(Gtemp)
    G = GAll[0]
    Gnodes = GAll[1]
    print(G)
    print(G.nodes())
    # A = nx.nx_agraph.to_agraph(G)

    posit = nx.planar_layout(G)
    nx.draw(G, posit, with_labels=True)

    resMap = open('cuatrocolores.txt', 'a')
    resMap.write(G.nodes(data=True).__str__())
    resMap.close()



    plt.savefig('graph.png')
    # fig.draw()
    # A.layout('dot')
    # A.draw('graph.png')



    # G = nx.Graph()
    # G.add_edges_from([('A', 'AM'), ('R', 'AM')])


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
