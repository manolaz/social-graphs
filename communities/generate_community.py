import networkx as nx
from py3plex.core import multinet
from py3plex.core import random_generators

## initiate an instance of a random graph -> this will produce a multiplex
ER_multilayer = random_generators.random_multiplex_ER(500,
                                                      8,
                                                      0.05,
                                                      directed=False)

## simple networkx object
aggregated_network = ER_multilayer.aggregate_edges(metric="count",
                                                   normalize_by="degree")
print(nx.info(aggregated_network))

## unnormalized counts for edge weights
aggregated_network = ER_multilayer.aggregate_edges(metric="count",
                                                   normalize_by="raw")
print(nx.info(aggregated_network))