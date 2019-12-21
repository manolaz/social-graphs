package user;

import java.time.Instant;
import java.util.*;
import java.util.stream.IntStream;

public class GraphImproved extends BaseGraph {
    // adjacency list of edges
    private List<List<Edge>> edges;

    // vector of vertices in
    private List<Vertex> vertices;

    private static Random rand = new Random();

    public GraphImproved() {
        edges = new ArrayList<>();
        vertices = new ArrayList<>();
    }

    public List<Vertex> getVertices() {
        return vertices;
    }

    public void addVertex(Vertex v) {
        vertices.add(v);
    }

    public void addEdge(Vertex from, Vertex to, double weight) {
        // Improve 3: Due to improve 1 and 2, we don't need to traversal all edges to check the existing.
        // We can ignore below loop to save a lot of time
//        for (Edge e : edges.get(from.id())) {
//            if (e.from() == from && e.to() == to || e.from() == to && e.to() == from) {
//                return; // already has an edge, return
//            }
//        }

        edges.get(from.id()).add(new Edge(from, to, weight));
        edges.get(to.id()).add(new Edge(to, from, weight));
    }

    public void printGraph() {
        for (List<Edge> vList : edges) {
            if (vList.size() > 0) {
                System.out.print("" + vList.get(0).from().id());
                for (Edge edge : vList) {
                    System.out.print(String.format(" (%d, %d, %.0f)", edge.from().id(), edge.to().id(), edge.weight()));
                }
                System.out.println();
            }
        }
    }

    public static GraphImproved genRandomNetwork(int nUsers, int nFriends) {
        nFriends = Math.min(nUsers - 1, nFriends);

        System.out.println(String.format("genRandomNetwork(nUsers = %d, nFriends = %d)", nUsers, nFriends));
        long curTime = Instant.now().toEpochMilli();
        GraphImproved g = new GraphImproved();

        // step 1: create vertices (users)
        IntStream.range(0, nUsers).forEach(i -> {
            g.addVertex(new Vertex(i));
            g.edges.add(new ArrayList<>());
        });
        System.out.println("  -> Create vertices takes: " + (Instant.now().toEpochMilli() - curTime) + " ms");

        // step 2: add edges (friends)
        curTime = Instant.now().toEpochMilli();
        for (Vertex v : g.vertices) {
            IntStream.range(0, nFriends).forEach(i -> {
                int idx = rand.nextInt(nUsers);
                while (idx == v.id()) {
                    idx = rand.nextInt(nUsers);
                }
                g.addEdge(v, g.vertices.get(idx), 1.0);
            });
        }
        System.out.println("  -> Add edges takes: " + (Instant.now().toEpochMilli() - curTime) + " ms");
        return g;
    }

    public static GraphImproved genNetwork(int nCommunity, int nMember) {
        System.out.println(String.format("createGraph(nCommunity = %d, nMember = %d)", nCommunity, nMember));
        long curTime = Instant.now().toEpochMilli();
        GraphImproved g = new GraphImproved();

        // step 1: add mandatory requirement (n communities, each has m members)
        IntStream.range(0, nCommunity).forEach(i -> {
            IntStream.range(0, nMember).forEach(j -> {
                Vertex v = new Vertex(i * nMember + j);
                g.addVertex(v);
                g.edges.add(new ArrayList<>());
            });

            for (int t = 0; t < nMember; t++) {
            	// Improve 1: Make friend is kind of un-directed graph (follow is directed), so we don't need to make 2-ways edges
				// Therefore, t2 starts from {t + 1}
                for (int t2 = t + 1; t2 < nMember; t2++) {
                	// Improve 2: t2 starts from {t + 1} and t2 always increases -> t2 > t all the time.
                    // if (t != t2) {
					g.addEdge(g.vertices.get(i * nMember + t), g.vertices.get(i * nMember + t2), 1.0);
                    //}
                }
            }
        });
        System.out.println("  -> Add links takes: " + (Instant.now().toEpochMilli() - curTime) + " ms");

        // step 2: add random links between those community
        curTime = Instant.now().toEpochMilli();
        IntStream.range(0, nCommunity).forEach(i -> {
            g.addEdge(g.vertices.get(rand.nextInt(i * nMember + nMember)),
                    g.vertices.get(rand.nextInt(nCommunity * nMember)), 1.0);
        });

        System.out.println("  -> Add more links takes: " + (Instant.now().toEpochMilli() - curTime) + " ms");
        return g;
    }

    public List<Set<Vertex>> findAllCommunities(int size){
        List<Set<Vertex>> maxCommunities = new ArrayList<Set<Vertex>>();

        for (Set<Vertex> set: BronKerbosch.maximalCliques(this))
            if (set.size() > size) {
                maxCommunities.add(set);
            }

        maxCommunities.sort(new Comparator<Set<Vertex>>() {
            @Override
            public int compare(final Set<Vertex> s1, final Set<Vertex> s2) {
                return Integer.compare(s1.size(), s2.size());
            }
        });

        return maxCommunities;
    }

    @Override
    List<List<Edge>> getEdges() {
        return edges;
    }

    @Override
    Map<Vertex, HashSet<Vertex>> getAdjList() {
        return null;
    }
}
