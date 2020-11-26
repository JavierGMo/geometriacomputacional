import networkx as nx
import matplotlib.pyplot as plt

graph = {'s1': ['v', 't1','w'],
     's2': ['t1','s1'],
     's3': ['v','w'],
     's4': ['x','y'],
     'x': ['v','w'],
     'v': ['t1', 'w'],
     'w': ['y','t1','t2'],
     'y': ['v','t1','t2'],
     't1': [],
     't2': []
     }

def main(G):
    fig = plt.figure()
    fig.show()

    graph = nx.DiGraph()
    for v in G.keys():
        graph.add_node(v)

    for delta in G.items():
        for w in delta[1]:
            graph.add_edge(delta[0],w)

    #posit = nx.shell_layout(G) #ISN'T NEEDED ANYMORE

    
    print(graph.edges)
    print(graph.nodes)

    nx.draw_planar(graph,with_labels = True, alpha=0.8) #NEW FUNCTION
    plt.savefig('test.png')


main(graph)