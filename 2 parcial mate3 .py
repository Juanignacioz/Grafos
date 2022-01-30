import re  
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import info

info = [('a', 'b', 6),
    ('a', 'd', 2), 
    ('a', 'h', 5),
    ('b', 'c', 7),
    ('b', 'e', 8),
    ('b', 'g', 11),
    ('c', 'g', 4),
    ('d', 'a', 9),
    ('d', 'c', 3),
    ('d', 'f', 5),
    ('e', 'd', 6),
    ('e', 'h', 12),
    ('f', 'b', 2),
    ('f', 'g', 9)]

# se pisan los datos de AD y DA
 
class Grafo:
    
    def __init__(self, ininfo):
        self.info = ininfo
    
    def respuesta(self):

        G = nx.Graph()
        self.cargoGraph(G, self.info)
        print("Vecinos: ", list(G.neighbors('h')))
        print("Cantidad de aristas de cada nodo: ",G.degree()) 
        print(dict(G.degree()))
        AD = nx.adjacency_matrix(G)
        print(AD.todense()) 
        I =  nx.incidence_matrix(G)
        print(I.todense())
        print("Valores de los enlaces del nodo: ",G['c'])
        print("Longitud de Ruta ponderada más corta desde el nodo:", nx.single_source_dijkstra_path_length(G,'c'))
        print("Promedio de la ruta mas corta ", nx.algorithms.average_shortest_path_length(G, method="floyd-warshall"))
        print("Ruta mas corta usando el algoritmo de Dijkstra entre:",nx.algorithms.dijkstra_path(G, 'a', 'h'))
        print("Longitud de Ruta ponderada más corta entre es :",nx.dijkstra_path_length(G,'a','h'))
        print("Longitud de Ruta ponderada más corta desde el nodo:", nx.single_source_dijkstra_path_length(G,'g'))
        print("Radio:",nx.radius(G))
        print("Diámetro:", nx.diameter(G))
        print("Excentricidad:", nx.eccentricity(G))
        print("Centro:", nx.center(G))
        print("Periferia:", nx.periphery(G))
        print("Densidad:", nx.density(G))
        pos = nx.shell_layout(G)
        self.emitoGraph(G, pos)
        H = G.to_directed()
        self.cargoGraph(H, self.info)
        pos = nx.shell_layout(H)
        self.emitoGraph(H, pos)


    def emitoGraph(self, G, pos):

        nx.draw_networkx_nodes(G, pos, node_color='Grey', node_size=400)
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='cursive')
        nx.draw_networkx_edges(G, pos, edge_color='red', width=2, arrowstyle= '<|-|>', arrowsize = 15)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis('off')  
        plt.show()

    def cargoGraph(self, G, ininfo):
       G.add_weighted_edges_from(info) 
    




grafo = Grafo(info)
grafo.respuesta()


# # Ejercicio 3 REGEX 

Texto = """ 1.AEP;CNQ;95.45;680.00
            2.EZE;IRJ;39.50;4780.00
            3.JNI;COC;51.44;1160.00
            4.LPG;AEP;66.26;7580.00
            5.MDQ;GPO;18.85;720.00
            6.FDO;RYO;26.49;340.00 """   

buscar =r"([\w]{3}\;[0-9]{2}\.[0-9]{2})"

print("\nEjercicio 3 :\n")
print(re.findall(buscar, Texto))    
