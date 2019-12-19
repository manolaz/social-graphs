from py3plex.algorithms.community_detection import community_wrapper as cw
from py3plex.core import multinet
from py3plex.visualization.multilayer import *
from py3plex.visualization.colors import colors_default
from collections import Counter

from py3plex.core import random_generators

network_size = int(input("Network total nodes = "))
network_density = int(input("Network connections density = "))
## initiate an instance of a random graph -> this will produce a multiplex
ER_multilayer = random_generators.random_multiplex_ER(network_size,
                                                      network_density,
                                                      0.05,
                                                      directed=False)

## simple networkx object
network = ER_multilayer.aggregate_edges(metric="count",
                                                   normalize_by="degree")
print(nx.info(network))

##################################
# THE LOUVAIN ALGORITHM
##################################

partition = cw.louvain_communities(network)
# print(partition)
# select top n communities by size
top_n = 20
partition_counts = dict(Counter(partition.values()))
top_n_communities = list(partition_counts.keys())[0:top_n]

print(partition_counts)
print(top_n_communities)
# # assign node colors
# color_mappings = dict(
#     zip(top_n_communities,
#         [x for x in colors_default if x != "black"][0:top_n]))

# network_colors = [
#     color_mappings[partition[x]]
#     if partition[x] in top_n_communities else "black"
#     for x in network.nodes()
# ]
# print(network_colors)


# visualize the network's communities!
# hairball_plot(network.core_network,
#               color_list=network_colors,
#               layout_parameters={"iterations": args.iterations},
#               scale_by_size=True,
#               layout_algorithm="force",
#               legend=False)
# plt.show()
