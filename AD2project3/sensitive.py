#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 3: Controlling Maximum Flow

Team Number: 22
Student Names: Christoffer Falkovén, Alfred Lindholm
'''

import unittest
import networkx as nx

# API for networkx flow algorithms changed in v1.9:
if list(map(lambda x: int(x), nx.__version__.split("."))) < [1, 9]:
    max_flow = nx.ford_fulkerson
else:
    max_flow = nx.maximum_flow
"""
We use max_flow() to generate flows for the included tests,
and you may of course use it as well in any tests you generate.
As always, your implementation of the senstive() function may NOT make use
of max_flow(), or any of the other graph algorithm implementations
provided by networkx.
"""

# If your solution needs a queue (like the BFS algorithm), you can use this one:
from collections import deque

try:
    import matplotlib.pyplot as plt

    HAVE_PLT = True
except ImportError:
    HAVE_PLT = False

"""
F is represented in python as a dictionary of dictionaries;
i.e., given two nodes u and v,
the computed flow from u to v is given by F[u][v].
"""


class SensitiveSanityCheck(unittest.TestCase):
    """
    Test suite for the sensitive edge problem
    """

    def draw_graph(self, H, u, v, flow1, F1, flow2, F2):
        if not HAVE_PLT:
            return
        pos = nx.spring_layout(self.G)
        plt.subplot(1, 2, 1)
        plt.axis('off')
        nx.draw_networkx_nodes(self.G, pos)
        nx.draw_networkx_edges(self.G, pos)
        nx.draw_networkx_labels(self.G, pos)
        nx.draw_networkx_edge_labels(
            self.G, pos,
            edge_labels={(u, v): '{}/{}'.format(
                F1[u][v],
                self.G[u][v]['capacity']
            ) for (u, v, data) in nx.to_edgelist(self.G)})
        plt.title('before: flow={}'.format(flow1))
        plt.subplot(1, 2, 2)
        plt.axis('off')
        nx.draw_networkx_nodes(self.G, pos)
        nx.draw_networkx_edges(self.G, pos)
        nx.draw_networkx_edges(
            self.G, pos,
            edgelist=[(u, v)],
            width=3.0,
            edge_color='b')
        nx.draw_networkx_labels(self.G, pos)
        nx.draw_networkx_edge_labels(
            self.G, pos,
            edge_labels={(u, v): '{}/{}'.format(
                F2[u][v], H[u][v]['capacity']
            ) for (u, v, data) in nx.to_edgelist(self.G)})
        plt.title('after: flow={}'.format(flow2))

    def setUp(self):
        """start every test with an empty directed graph"""
        self.G = nx.DiGraph()

    def run_test(self, s, t, draw=False):

        """standard tests to run for all cases

        Uses networkx to generate a maximal flow
        """
        H = self.G.copy()
        # compute max flow
        flow_g, F_g = max_flow(self.G, s, t)
        # find a sensitive edge
        u, v = sensitive(self.G, s, t, F_g)
        # is u a node in G?


        self.assertIn(u, self.G, "Invalid edge ({}, {})".format(u, v))
        # is (u,v) an edge in G?
        self.assertIn(v, self.G[u], "Invalid edge ({}, {})".format(u, v))
        # decrease capacity of (u,v) by 1
        H[u][v]["capacity"] = H[u][v]["capacity"] - 1
        # recompute max flow
        flow_h, F_h = max_flow(H, s, t)
        if draw:
            self.draw_graph(H, u, v, flow_g, F_g, flow_h, F_h)
        # is the new max flow lower than the old max flow?
        self.assertLess(
            flow_h,
            flow_g,
            "Returned non-sensitive edge ({},{})".format(u, v))

    def test_sanity(self):
        """Sanity check"""
        # The attribute on each edge MUST be called "capacity"
        # (otherwise the max flow algorithm in run_test will fail).
        self.G.add_edge(0, 1, capacity=16)
        self.G.add_edge(0, 2, capacity=13)
        self.G.add_edge(2, 1, capacity=4)
        self.G.add_edge(1, 3, capacity=12)
        self.G.add_edge(3, 2, capacity=9)
        self.G.add_edge(2, 4, capacity=14)
        self.G.add_edge(4, 3, capacity=7)
        self.G.add_edge(3, 5, capacity=20)
        self.G.add_edge(4, 5, capacity=4)
        self.run_test(0, 5, draw=True)

    @classmethod
    def tearDownClass(cls):
        if HAVE_PLT:
            plt.show()


# Based on Apollo's code https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3

def breadth_first_search(source, F):
    """
        Sig:    int, int[0..|V|-1, 0..|V|-1] ==> int[0..|V|-1, 0..|V|-1]
        Pre:    F is nested dictionary that contain all nodes and vertices of a positive weighted, directed graph.
                There is a single source node s ∈ F.
        Post:   A list of all nodes in F reachable from source
        Ex:
                G = nx.complete_graph(3, create_using=nx.DiGraph());
                G.remove_edge(0, 1)
                G.remove_edge(1, 2)
                G.remove_edge(2, 0)
                G.remove_edge(1, 0)
                source = 0
                t = 1
                flow_g, F_g = max_flow(G, source, t)
                breadth_first_search(source, F_g) ==> [0,1,2]
    """
    # Initialize the visited set with the source node.
    visited = {source}
    # Add the source node to the queue
    queue = list([source])
    # Initialize an empty list for the function to put its results into later.
    bfs = []
    # Loop over all the elements in the queue until the queue is empty.
    # Variant: Len(queue)
    # Invariant: Len(queue) = 0
    while queue:
        # Pop the leftmost element in the queue.
        vertex = queue.pop(0)
        # Append that element into the bfs list.
        bfs.append(vertex)
        # Start a for-loop to go through all the neighbors of your vertex node.
        # Variant: Len(F[vertex])
        for node in F[vertex]:
            # Check if the neighbor has been visited before or not.
            if node not in visited:
                # If the neighbor has not been visited then add it to the visited set.
                visited.add(node)
                # Append that neighbor to the queue.
                queue.append(node)
    # Return the list containing all nodes in F reachable from the source node "source".
    return bfs


def sensitive(G, s, t, F):
    """
        Sig:    graph G(V,E), int, int, int[0..|V|-1, 0..|V|-1] ==> int, int
        Pre:    G is a positive weighted, directed graph. There is a single source node s ∈ G and there is a single sink node t ∈ G.
        Post:   A tuple (u, v) containing two connected nodes that make up a sensitive edge or a tuple containing (None, None) if no
                sensitive edges are present in the graph.
        Ex:
                G = nx.complete_graph(3, create_using=nx.DiGraph());
                G.remove_edge(0, 1)
                G.remove_edge(1, 2)
                G.remove_edge(2, 0)
                G.remove_edge(1, 0)
                G[0][2]['capacity'] = 2
                G[2][1]['capacity'] = 6
                s = 0
                t = 1
                flow_g, F_g = max_flow(G, s, t)
                sensitive(G.copy(), s, t, F_g) ==> (0, 2)


                G = nx.complete_graph(7, create_using=nx.DiGraph());
                G.remove_edge(0, 1)
                G.remove_edge(0, 2)
                G.remove_edge(0, 3)
                G.remove_edge(0, 6)
                G.remove_edge(1, 2)
                G.remove_edge(1, 4)
                G.remove_edge(1, 5)
                G.remove_edge(2, 6)
                G.remove_edge(3, 1)
                G.remove_edge(3, 2)
                G.remove_edge(3, 4)
                G.remove_edge(3, 5)
                G.remove_edge(3, 6)
                G.remove_edge(4, 0)
                G.remove_edge(4, 2)
                G.remove_edge(4, 5)
                G.remove_edge(4, 6)
                G.remove_edge(5, 0)
                G.remove_edge(5, 2)
                G.remove_edge(6, 1)
                G.remove_edge(6, 5)
                G.remove_edge(1, 3)
                G.remove_edge(2, 3)
                G.remove_edge(4, 3)
                G.remove_edge(5, 3)
                G.remove_edge(6, 3)
                G.remove_edge(2, 0)
                G.remove_edge(2, 1)
                G.remove_edge(2, 4)
                G.remove_edge(2, 5)

                G[0][4]['capacity'] = 89
                G[0][5]['capacity'] = 33
                G[1][0]['capacity'] = 64
                G[1][6]['capacity'] = 195
                G[3][0]['capacity'] = 153
                G[4][1]['capacity'] = 24
                G[5][1]['capacity'] = 75
                G[5][4]['capacity'] = 77
                G[5][6]['capacity'] = 5
                G[6][0]['capacity'] = 108
                G[6][2]['capacity'] = 41
                G[6][4]['capacity'] = 164
                s = 3
                t = 2
                flow_g, F_g = max_flow(G, s, t)
                sensitive(G.copy(), s, t, F_g) ==> (6, 2)

    """
    # Initialize the source set of the s-t cut to contain the source/starting node.
    s_visited = [s]
    # Do a breadth first search and add all nodes in G into the t-cut of the s-t cut.
    t_not_visited = breadth_first_search(s, F)
    # Since an s-t cut will always have the source node in the s-cut and the sink node, t, in the t-cut we remove the
    #  sink node from the t-cut immediately.
    t_not_visited.remove(s)
    # Initialize the visited set to contain the sink node.
    visited = {s}
    # Add the sink node to the queue
    queue = list([s])
    # Loop over all the elements in the queue until the queue is empty.
    # Variant: Len(queue)
    # Invariant: Len(queue) = 0
    while queue:
        # Pop the first element of the queue and add it into a variable we call vertex.
        vertex = queue.pop(0)
        # Start a for-loop to go through all the neighbors of your vertex node.
        # Variant: Len(F[vertex])
        for node in F[vertex]:
            # Initialize a variable e to contain two connected nodes.
            e = (vertex, node)
            # Check whether the weight connecting your vertex and the current neighbor is equal to the capacity of
            # the two nodes or not.
            if F[vertex][node] != G.get_edge_data(*e)['capacity']:
                # Check if that neighbor is already in the sink set or not already.
                if node in t_not_visited:
                    # If that node is in the sink set then remove it from there.
                    t_not_visited.remove(node)
                # Check if the node is in the source set or not.
                if node not in s_visited:
                    # If the neighbor is not the the source set then add it.
                    s_visited.append(node)
                # Check if the neighbor has been visited before or not.
                if node not in visited:
                    # If the neighbor has not been visited then add it to the visited set.
                    visited.add(node)
                    # Append that neighbor to the queue.
                    queue.append(node)

        # Create a variable that holds all predecessors to the vertex that you're currently on. (I.E create back-edges).
        back_flow = list(G.predecessors(vertex))
        # Loop over all of the nodes that has some kind of flow pointing towards your current vertex.
        # Variant: Len(back_flow)
        for nodes in back_flow:
            # Only check the nodes that has a possibility of having an back-edge flow to your vertex (I.E has a flow
            # larger than 0).
            if F[nodes][vertex] > 0:
                # Check if the predecessor node with a positive flow is in the sink cut of the s-t cut.
                if nodes in t_not_visited:
                    # If it is then remove it from the sink cut.
                    t_not_visited.remove(nodes)
                # Check if the predecessor node with a positive flow is not in the source cut of the s-t cut.
                if nodes not in s_visited:
                    # If it is not present, then add it to the source cut.
                    s_visited.append(nodes)
                # Check if the predecessor node has been visited before.
                if nodes not in visited:
                    # If it never has, then add it to the visited set.
                    visited.add(nodes)
                    # Append the predecessor node to the queue.
                    queue.append(nodes)

    # Loop over all the elements that are in the source set of the s-t cut.
    # Variant: Len(s_visited)
    for node in s_visited:
        # Nested loop that loops over all of the nodes that are in the sink set of the s-t cut.
        # Variant: Len(t_not_visited)
        for nodes in t_not_visited:
            # Try and catch statement that check if any of the nodes in the s-t cut are connected, if they are then
            # return those two nodes as they must be a sensitive edge. Have a catch statement so not to trigger a bad
            # KeyError.
            try:
                if F[node][nodes]:
                    return node, nodes
            except KeyError:
                print "Bad key, ignore"
    # If you failed to find a sensitive edge, then return None, None.
    return None, None


if __name__ == "__main__":
    unittest.main()
