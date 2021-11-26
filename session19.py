#%%

graph = {
    1: [2,3,4],
    2: [5,6],
    3: [],
    4: [7, 8],
    5: [],
    6: [],
    7: [],
    8: []
}

# [1,2,34,5,6]
def bfs(graph, start):
    queue = [start]
    visited = []

    while len(queue) != 0:
        current = queue[0]
        queue.pop(0)
        neighbors = graph[current]
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
        visited.append(current)

    return visited


print(bfs(graph, 1))

# %%



graph = {
    1: [2,3,4],
    2: [5,6],
    3: [],
    4: [7, 8],
    5: [],
    6: [],
    7: [],
    8: []
}

# returns 
# {
#    1: [1],
#    2: [1, 2],
#    4: [1, 4],
#    ...
#    8: [1, 4, 8]
# }
def find_all_paths(graph, start):
    queue = [start]
    paths = {start: [start]}

    while queue != []:
        current = queue[0]
        queue.pop(0)
        neighbors = graph[current]
        for neighbor in neighbors:
            if neighbor not in paths:
                paths[neighbor] = paths[current] + [neighbor]
                queue.append(neighbor)

    return paths

print(find_all_paths(graph, 1))
# %%

def find_path(graph, start, end):
    paths = find_all_paths(graph, start)

    if end in paths:
        return paths[end]
    else:
        return None


# NOT MANDATORY
#
# Edsger Dijkstra
#   Dijkstra's algo
#   A* algo

print(find_path(graph, 1, 8))
# %%

import networkx as nx

graph = nx.DiGraph()

graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(3, 5)

print(nx.shortest_path(graph, 1, 5))
# %%
