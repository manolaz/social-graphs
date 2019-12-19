def random_multiplex_ER(n, l, p, directed=False):
    """ random multilayer ER """

    if directed:
        G = nx.MultiDiGraph()
    else:
        G = nx.MultiGraph()

    for lx in range(l):
        network = nx.fast_gnp_random_graph(n, p, seed=None, directed=directed)
        for edge in network.edges():
            G.add_edge((edge[0], lx), (edge[1], lx), type="default")

    ## construct the ppx object
    no = multi_layer_network(network_type="multiplex").load_network(
        G, input_type="nx", directed=directed)
    return no