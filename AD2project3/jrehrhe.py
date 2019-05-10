#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 3: Controlling Maximum Flow

Team Number:
Student Names:
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

#
# def sensitive(G, s, t, F):
#     """
#     Sig:   graph G(V,E), int, int, int[0..|V|-1, 0..|V|-1] ==> int, int
#     Pre:
#     Post:
#     Ex:    sensitive(G,0,5,F) ==> (1, 3)
#     """
#
#     return None, None


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
        print "capacity of 0-1: " + str(H[0][1]["capacity"])
        print "capacity of 0-2: " + str(H[0][2]["capacity"])
        print "capacity of 2-1: " + str(H[2][1]["capacity"])
        print "capacity of 1-3: " + str(H[1][3]["capacity"])
        print "capacity of 2-4: " + str(H[2][4]["capacity"])
        print "capacity of 3-2: " + str(H[3][2]["capacity"])
        print "capacity of 4-3: " + str(H[4][3]["capacity"])
        print "capacity of 3-5: " + str(H[3][5]["capacity"])
        print "capacity of 4-5: " + str(H[4][5]["capacity"])


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

def breath_first_search(source, F):
    seen = {source}
    queue = list([source])
    bfs = []
    while queue:
        vertex = queue.pop(0)
        bfs.append(vertex)
        for node in F[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)
    return bfs


# Based on Apollo's code https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3
def sensitive(G, s, t, F):
    s_visited = [s]
    t_not_visited = breath_first_search(s, F)
    t_not_visited.remove(s)
    seen = {s}
    queue = list([s])
    bfs = []
    while queue:
        vertex = queue.pop(0)
        bfs.append(vertex)
        print "¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤"
        for node in F[vertex]:
            e = (vertex, node)
            print e
            print G.get_edge_data(*e)['capacity']
            print F[vertex][node]
            if F[vertex][node] != G.get_edge_data(*e)['capacity']:
                #print t_not_visited
                #print s_visited
                # print node
                if node in t_not_visited:
                    t_not_visited.remove(node)
                if node not in s_visited:
                    s_visited.append(node)

            if node not in seen:
            #     print "the vertex is: "
            #     print vertex
            #     print "the node is: "
            #     print node
            #     print G.get_edge_data(*e)['capacity']
            #     print "ahajajaja"
            #     print F[vertex][node]
            #     if F[vertex][node] == G.get_edge_data(*e)['capacity']:
            #         t_not_visited.remove(node)
            #         s_visited.append(node)

                seen.add(node)
                queue.append(node)

    if t not in t_not_visited:
        t_not_visited.append(t)
    if t in s_visited:
        s_visited.remove(t)

    print F
    for node in s_visited:
        print "yeeboiiiiiis"
        print F[node]
        for nodes in t_not_visited:
            try:
                if F[node][nodes]:
                    print "mathc in "
                    return node, nodes
            except KeyError:
                print "nothing to see here"
    return None, None


    print "ALLL DONE MYDUDE"
    print "S equals: "
    print s_visited
    print "T equals: "
    print t_not_visited

    return None, None

    # s_visited = [s]
    # t_not_visited = breath_first_search(s, F)
    # t_not_visited.remove(s)
    # print "inne i sensitive"
    # print t_not_visited
    # print s_visited
    #
    # for vertex in t_not_visited:
    #     print vertex
    #     vertex = t_not_visited[vertex]
    #     # for node in F[vertex]:
    #     #     print
    #     #     e = (vertex, node)
    #     #     # print G.get_edge_data(*e)['capacity']
    #     #     # print "ahajajaja"
    #     #     # print F[vertex][node]
    #     #     if F[vertex][node] == G.get_edge_data(*e)['capacity']:
    #     #         # print "inne i if grejen "
    #     #         # print "printing F[vertex][node]"
    #     #         # print F[vertex][node]
    #     #         # print "G.get_edge_data(*e) "
    #     #         # print G.get_edge_data(*e)
    #     #         # print "t_not_visited: " + str(t_not_visited)
    #     #         # print t_not_visited
    #     #         # print node
    #     #         # print "s_visited: " + str(s_visited)
    #     #         if node in t_not_visited:
    #     #             t_not_visited.remove(node)
    #     #         if node not in s_visited:
    #     #             s_visited.append(node)
    #
    # if len(t_not_visited) >= 2:
    #     # print "pisssssssssssssssssssssssssssssssssssssssss"
    #     # print "ALLL DONE MYDUDE"
    #     # print "S equals: "
    #     # print s_visited
    #     # print "T equals: "
    #     # print t_not_visited
    #     (x, y) = s_visited[0], s_visited[1]
    #     return x, y


    print "ALLL DONE MYDUDE"
    print "S equals: "
    print s_visited
    print "T equals: "
    print t_not_visited
    return None, None



if __name__ == "__main__":
    # unittest.main()
    # G = nx.Graph()
    # G.add_edge(0, 1, capacity=16)
    # G.add_edge(0, 2, capacity=13)
    # G.add_edge(2, 1, capacity=4)
    # G.add_edge(1, 3, capacity=12)
    # G.add_edge(3, 2, capacity=9)
    # G.add_edge(2, 4, capacity=14)
    # G.add_edge(4, 3, capacity=7)
    # G.add_edge(3, 5, capacity=20)
    # G.add_edge(4, 5, capacity=4)
    # flow_g, F_g = max_flow(G, 0, 5)
    # print flow_g
    # print "%%%%%%%%%"
    # print F_g
    # print "&&&&&-SENSITIVE-&&&&&"
    # # sensitive(G,0,5,F) ==> (1, 3)
    # source = 0
    # sink = 5
    # result = sensitive(G, source, sink, F_g)
    # print "YEEEEEEEEEEEEET"
    # print result

    #print breath_first_search(source, F_g, G)
    # if (list(map(lambda x: int(x), nx.__version__.split("."))) < [1, 9]):
    #     max_flow = nx.ford_fulkerson
    # else:
    #     max_flow = nx.maximum_flow
    # G = nx.complete_graph(6, create_using=nx.DiGraph());
    #
    # G.remove_edge(0, 1)
    # G.remove_edge(0, 3)
    # G.remove_edge(0, 4)
    # G.remove_edge(0, 5)
    # G.remove_edge(1, 3)
    # G.remove_edge(2, 0)
    # G.remove_edge(2, 1)
    # G.remove_edge(2, 3)
    # G.remove_edge(2, 4)
    # G.remove_edge(3, 5)
    # G.remove_edge(4, 1)
    # G.remove_edge(4, 3)
    # G.remove_edge(4, 5)
    # G.remove_edge(5, 1)
    # G.remove_edge(5, 2)
    # G.remove_edge(5, 3)
    # G.remove_edge(5, 0)
    # G.remove_edge(5, 4)
    #
    # G[0][2]['capacity'] = 93
    # G[1][0]['capacity'] = 94
    # G[1][2]['capacity'] = 15
    # G[1][4]['capacity'] = 74
    # G[1][5]['capacity'] = 22
    # G[2][5]['capacity'] = 89
    # G[3][0]['capacity'] = 51
    # G[3][1]['capacity'] = 13
    # G[3][2]['capacity'] = 55
    # G[3][4]['capacity'] = 96
    # G[4][0]['capacity'] = 13
    # G[4][2]['capacity'] = 70
    #
    # s = 3
    # t = 5
    # flow_g, F_g = max_flow(G, s, t)
    # u, v = sensitive(G.copy(), s, t, F_g)
    # G[u][v]["capacity"] = (G[u][v]["capacity"]) - 1
    #
    # new_flow_g, new_F_g = max_flow(G, s, t)
    # print new_flow_g
    # print flow_g
    print "hej"
