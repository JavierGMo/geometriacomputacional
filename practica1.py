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

    for graph in Gtemp:
        for tmp in Gtemp:
            # print(Gtemp.nodes[graph]['colorN'])
            if Gtemp.nodes[tmp]['colorN'] != Gtemp.nodes[graph]['colorN']:
                Gnew.add_edge('{}'.format(graph), '{}'.format(tmp))
                # G.add_edge('{}'.format(graph), '{}'.format(tmp))
    return (Gnew, Gtemp)

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
            # print('Count colors: {}, Color : {},iterator {}'.format(countColors, colorsMap[countColors], iterNumber))
            countColors = 0 if (countColors == 3) else incrementCounter(countColors)

    #Asignacion de ramas para cualquier caso mayor igual a 4
    return Gtemp

if __name__ == "__main__":
    fig = plt.figure()
    fig.show()
    G = mapNode()
    Gtemp = copy.deepcopy(G)
    GAll = mapBranch(Gtemp)
    G = GAll[0]
    Gnodes = GAll[1]

    # A = nx.nx_agraph.to_agraph(G)
    resMap = open('cuatrocolores.txt', 'a')
    resMap.write('Resultado de los cuatro colores \n')
    resMap.write('Nodos del grafo: \n')
    resMap.write(Gnodes.nodes(data=True).__str__())
    resMap.write('Cuatro colores \n')
    resMap.write('\nRamas: \n')
    for branch in G.edges(data=True):
        resMap.write('{}\n'.format(branch.__str__()))
    # resMap.write(G.edges(data=True).__str__())
    resMap.close()
    try:
        posit = nx.planar_layout(G)
        nx.draw(G, posit, with_labels=True)
        plt.savefig('graph.png')
    except:
        resMap = open('errorplanar.txt', 'a')
        resMap.write('Error en la construccion del grafo, pero se confirma la teoria de los cuatro colores')
        resMap.close()

    