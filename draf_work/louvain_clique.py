import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

# G = nx.erdos_renyi_graph(100, 0.01)
#first compute the best partition
#better with karate_graph() as defined in networkx example. #erdos renyi don't have true community structure
G = nx.erdos_renyi_graph(30, 0.05)
partition = community.best_partition(G)

# G = nx.barbell_graph(5, 1)
# communities_generator = community.girvan_newman(G)
# top_level_communities = next(communities_generator)
# next_level_communities = next(communities_generator)
# sorted(map(sorted, next_level_communities))

#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0
for com in set(partition.values()) :
    count = count + 1
    list_nodes = [nodes for nodes in partition.keys()
        if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
            node_color=str(count / size))
            
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()