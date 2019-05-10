def breadth_first_search(source, F):
    visited = {source}                                                                  # O(1)
    queue = list([source])                                                              # O(1)
    bfs = []                                                                            # O(1)
    while queue:                                                                        # O(V)
        vertex = queue.pop(0)                                                           # O(1)
        bfs.append(vertex)                                                              # O(1)
        for node in F[vertex]:                                                          # O(V)
            if node not in visited:                                                     # O(V)
                visited.add(node)                                                       # O(1)
                queue.append(node)                                                      # O(1)
    return bfs                                                                          # O(1)
                                                                                 # Total: O(V + E)

def sensitive(G, s, t, F):
    s_visited = [s]                                                                     # O(1)
    t_not_visited = breadth_first_search(s, F)                                          # O(V + E)
    t_not_visited.remove(s)                                                             # O(1)
    visited = {s}                                                                       # O(1)
    queue = list([s])                                                                   # O(1)
    while queue:                                                                        # O(V)
        vertex = queue.pop(0)                                                           # O(1)
        for node in F[vertex]:                                                          # O(V)
            e = (vertex, node)                                                          # O(1)
            if F[vertex][node] != G.get_edge_data(*e)['capacity']:                      # O(1)
                if node in t_not_visited:                                               # O(V)
                    t_not_visited.remove(node)                                          # O(1)
                if node not in s_visited:                                               # O(V)
                    s_visited.append(node)                                              # O(1)
                if node not in visited:                                                 # O(V)
                    visited.add(node)                                                   # O(1)
                    queue.append(node)                                                  # O(1)
        back_flow = list(G.predecessors(vertex))                                        # O(V)
        for nodes in back_flow:                                                         # O(V)
            if F[nodes][vertex] > 0:                                                    # O(1)
                if nodes in t_not_visited:                                              # O(V)
                    t_not_visited.remove(nodes)                                         # O(1)
                if nodes not in s_visited:                                              # O(V)
                    s_visited.append(nodes)                                             # O(1)
                if nodes not in visited:                                                # O(V)
                    visited.add(nodes)                                                  # O(1)
                    queue.append(nodes)                                                 # O(1)
    for node in s_visited:                                                              # O(V)
        for nodes in t_not_visited:                                                     # O(V)
            try:
                if F[node][nodes]:                                                      # O(1)
                    return node, nodes                                                  # O(1)
            except KeyError:
                print "Bad key, ignore"                                                 # O(1)
    return None, None                                                                   # O(1)




def breadth_first_search(source, F):
    visited = {source}
    queue = list([source])
    bfs = []
    while queue:
        vertex = queue.pop(0)
        bfs.append(vertex)
        for node in F[vertex]:
            if node not in visited:
                visited.add(node)
                queue.append(node)
    return bfs
