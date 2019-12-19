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
partition_counts = dict(Counter(partition.values()))

print("List of CLIQUE memberships levels : \n {}".format(partition_counts))

# select top n communities by size
# top_n = int(input("Max numbers of Communities to Select = "))
# top_n_communities = list(partition_counts.keys())[0:top_n]
# print("Total CLIQUE counted = {}".format(top_n_communities))