import community
import networkx as nx
import matplotlib.pyplot as plt
#better with karate_graph() as defined in networkx example. #erdos renyi don't have true community structure
G = nx.erdos_renyi_graph(30, 0.05)
#first compute the best partition
partition = community.best_partition(G)
#drawing
size = float(len(set(partition.values()))) pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
count = count + 1.
list_nodes = [nodes for nodes in partition.keys()
if partition[nodes] == com]