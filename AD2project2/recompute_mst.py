#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Recomputing the minimum spanning tree

Team Number:
Student Names:
'''
import unittest
import networkx as nx

"""IMPORTANT:
We're using networkx only to provide a reliable graph
object.  Your solution may NOT rely on the networkx implementation of
any graph algorithms.  You can use the node/edge creation functions to
create test data, and you can access node lists, edge lists, adjacency
lists, etc. DO NOT turn in a solution that uses a networkx
implementation of a graph traversal algorithm, as doing so will result
in a score of 0.
"""
try:
    import matplotlib.pyplot as plt

    have_plt = True
except:
    have_plt = False


def update_MST_1(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post:
    Example: TestCase 1
    """
    (u, v) = e
    assert (e in G.edges() and e not in T.edges() and w > G[u][v]['weight'])


def update_MST_2(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre: G is a connected, weighted, undirected graph with non-negative edge weights
         T is the minimum spanning tree of G
         w is less than w(e)
         e ∉ T
         e ∈ G
         T ⊆ G

    Post/side effect: An updated minimum spanning tree of G with the new weighted value of e.

    Example: TestCase 2
            G = G.add_edge('a', 'b', weight=0.6)
                G.add_edge('a', 'c', weight=0.2)
                G.add_edge('c', 'd', weight=0.1)
                G.add_edge('c', 'e', weight=0.7)
                G.add_edge('c', 'f', weight=0.9)
                G.add_edge('a', 'd', weight=0.3)

            T = nx.minimum_spanning_tree(G)     =   ('a', 'c') weight = {0.2}
                                                    ('a', 'b') weight = {0.6}
                                                    ('c', 'e') weight = {0.7}
                                                    ('c', 'd') weight = {0.1}
                                                    ('c', 'f') weight = {0.9}

            update_MST_2(G, T, ('a', 'd'), 0.1) ==> ('a', 'b') weight = {0.6}
                                                    ('a', 'd') weight = {0.1}
                                                    ('c', 'e') weight = {0.7}
                                                    ('c', 'd') weight = {0.1}
                                                    ('c', 'f') weight = {0.9}

    """

    # update_MST_2(G, T, ('a', 'd'), 0.1)
    (u, v) = e
    assert (e in G.edges() and e not in T.edges() and w < G[u][v]['weight'])
    # Connect the first node and second node in the tuple e with a weight of the specified weight-value, w, and add it to the tree T.
    T.add_edge(e[0], e[1], weight=w)
    # Check whether adding the edge, e, created a cycle in the tree T by using the ring_extended function that we made last assignment.
    # It returns tuple with a logical True if there exist a cycle followed by the nodes that form the cycle or False followed by an empty list if there is no
    # cycles present in T.
    ringT = ring_extended(T)
    # Checks whether the first element in the tuple is true, which means there is a cycle.
    if ringT[0]:
        # Creates a variable called nodes that contain all the unique nodes in the graph T that are part of the cycle.
        nodes = ringT[1]
        # Creates a variable that we call theRing that uses list comprehension to filter out all nodes that are not part of
        # the nodes in our cycle.

        # Variant: Len(T.edges(nodes))
        # Invariant: Len(T.edges(nodes) > 0
        theRing = [(edge1, edge2) for (edge1, edge2) in T.edges(nodes) if edge2 in nodes]
        # Initialize an empty list
        weightList= []
        # append all of the edges of the nodes in the cycle together with their weight in a tuple to the weightList that we initialize before.

        # Variant: Len(theRing)
        # Invariant: Len(theRing) > 0
        for edge in theRing:
            weightList.append((edge, T[edge[0]][edge[1]]['weight']))
        # Create a variable that filters out the highest second value of all the tuples from weightList.
        toRemove = max(weightList, key=lambda x: x[1])
        # Remove the tuple of nodes with the highest weight-cost from T. Leaving us a correct minimum spanning tree.
        T.remove_edge(*toRemove[0])



def update_MST_3(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post:
    Example: TestCase 3
    """
    (u, v) = e
    assert (e in G.edges() and e in T.edges() and w < G[u][v]['weight'])


def update_MST_4(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post:
    Example: TestCase 4
    """
    (u, v) = e
    assert (e in G.edges() and e in T.edges() and w > G[u][v]['weight'])


def ring_extended(G):
    """
    Sig:
        graph G(node,edge), list[int], Int, Int ==> boolean, int[0..j-1]
    Pre:
        The graph G cannot be empty.
        The graph G is made out of tuples of nodes and their connected edge.
        Each edge gets its own tuple.
    Post:
        A tuple containing a boolean statement followed by an list containing the first occurring cycle from the graph.
    Example:
        g1 = nx.Graph([(0, 1), (0, 2), (0, 3), (2, 4), (2, 5), (3, 6), (3, 7), (7, 8)])
        ring(g1) ==> False, []
                      0
                    / | \
                   1  2  3
                   |  |  |\
                   4  5  6 7
                            \
                             8
        g2 = nx.Graph([(0, 1), (0, 2), (0, 3), (2, 4), (2, 5), (3, 6), (3, 7), (7, 8), (6, 8)])
        ring(g2) ==>  True, [3,7,8,6,3]
                        0
                     / |  \
                    1  2   3
                    |  |  | \
                    4  5  6  7
                           \ \
                             8
    """
    # Initilize Int parent as NONE, since our first node does not have a parent node
    parent = None
    # Initilize List Visited, used to contain all the nodes that have already be expanded apon
    visited = []
    # Initilize Int start as the first node in the graph G.
    # start = list(G.nodes())[0]
    # Initilize List path, used to contain the nodes which build up the loop, if there is one.
    path = []
    # Call the first iteration of the recursive auxiliary function.
    for node in G.nodes():
        if node in visited:
            continue
        ourBool = ring_extended_aux(G, visited, node, parent, path)
        if ourBool[0]:
            return ourBool
    return False, []
    # return ring_extended_aux(G, visited, start, parent, path)


def ring_extended_aux(G, visited, start, parent, path):
    """
    Sig:
        graph G(node,edge), list[int], int, int, list ==> boolean, int[0..j-1]
    Pre:
        The graph G cannot be empty.
        The graph G is made out of tuples of nodes and their connected edge.
        Each edge gets its own tuple.
    Post:
        A tuple containing a boolean statement followed by an list containing the first occurring cycle from the graph.
    Example:
        g1 = nx.Graph([(0, 1), (0, 2), (0, 3), (2, 4), (2, 5), (3, 6), (3, 7), (7, 8)])
        ring_extended_aux(g1, [], 0, None, []) ==> False, []
        g2 = nx.Graph([(0, 1), (0, 2), (0, 3), (2, 4), (2, 5), (3, 6), (3, 7), (7, 8), (6, 8)])
        ring_extended_aux(g2, [], 0, None, []) ==>  True, [3,7,8,6,3]
    """
    # Insert the current node: start, into visited so that we dont return to it causing an infinite loop
    visited.append(start)
    # For each edge that the start node has attached to it, check if the destination node are in the visited list.
    # If they are and they are the parent node, continue through the next iteration of the FOR loop.
    # Otherwise, it means that there is a loop within the graph since the destination has been visited before and
    # its not the parent node. Then the destination is appended to path and  we return TRUE .
    # If however, the node has not been visited before, we recursively call ring_aux on that node
    # and return TRUE and append the destination to the path if that call returns TRUE. If none of these conditions occur, the
    # function returns False and the path unchanged.
    listOfEdges = G.edges(start)
    listOfEdges.sort(key=lambda x: x[1])

    for edge in listOfEdges:

        # Variant: Len(G.edges)
        # Invariant: Len(G.edges) > 0
        if edge[1] in visited:
            if edge[1] == parent:
                continue
            else:
                path.append(edge[1])
                return True, path
        else:
            if ring_extended_aux(G, visited, edge[1], start, path)[0]:
                if path[len(path)-1] == path[0] and len(path) > 1:
                    return True, path

                path.append(edge[1])
                return True, path
    if not path:
        return False, path
    else:
        return True, path



class RecomputeMstTest(unittest.TestCase):
    """Test Suite for minimum spanning tree problem

    Any method named "test_something" will be run when this file is
    executed. Use the sanity check as a template for adding your own
    test cases if you wish.
    (You may delete this class from your submitted solution.)
    """

    def create_graph(self):
        G = nx.Graph()
        G.add_edge('a', 'b', weight=0.6)
        G.add_edge('a', 'c', weight=0.2)
        G.add_edge('c', 'd', weight=0.1)
        G.add_edge('c', 'e', weight=0.7)
        G.add_edge('c', 'f', weight=0.9)
        G.add_edge('a', 'd', weight=0.3)
        return G

    def draw_mst(self, G, T, n):
        if not have_plt:
            return
        pos = nx.spring_layout(G)  # positions for all nodes
        plt.subplot(220 + n)
        plt.title('updated MST %d' % n)
        plt.axis('off')
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)
        # edges
        nx.draw_networkx_edges(G, pos, width=6, alpha=0.5,
                               edge_color='b', style='dashed')
        nx.draw_networkx_edges(T, pos, width=6)
        # labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    def test_mst1(self):
        """Sanity Test

        This is a simple sanity check for your function;
        passing is not a guarantee of correctness.
        """
        # TestCase 1: e in G.edges() and not e in T.edges() and
        #             w > G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_1(G, T, ('a', 'd'), 0.5)
        self.draw_mst(G, T, 1)
        self.assertItemsEqual(
            T.edges(),
            [('a', 'b'), ('a', 'c'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
        )

    def test_mst2(self):
        # TestCase 2: e in G.edges() and not e in T.edges() and
        #             w < G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)

        update_MST_2(G, T, ('a', 'd'), 0.1)
        self.draw_mst(G, T, 2)

        self.assertItemsEqual(
            T.edges(),
            [('a', 'b'), ('a', 'd'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
        )

    def test_mst3(self):
        # TestCase 3: e in G.edges() and e in T.edges() and
        #             w < G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_3(G, T, ('a', 'c'), 0.1)
        self.draw_mst(G, T, 3)
        self.assertItemsEqual(
            T.edges(),
            [('a', 'b'), ('a', 'c'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
        )

    def test_mst4(self):
        # TestCase 4: e in G.edges() and e in T.edges() and
        #             w > G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_4(G, T, ('a', 'c'), 0.4)
        self.draw_mst(G, T, 4)
        self.assertItemsEqual(
            T.edges(),
            [('a', 'b'), ('a', 'd'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
        )

    @classmethod
    def tearDownClass(cls):
        if have_plt:
            plt.show()


if __name__ == '__main__':
    unittest.main()
