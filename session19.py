#%% Graph defined using adjacency lists

graph = {
    1: [2,3,4],
    2: [5, 6],
    3: [],
    4: [7, 8],
    5: [],
    6: [],
    7: [],
    8: []
}


def bfs(graph, start):
    queue = [start]
    visited = []

    while queue != []:
        current = queue[0]
        queue.pop(0)
        for neighbor in graph[current]:
            # Q: why is this check required?
            if neighbor not in visited:
                queue.append(neighbor)

        visited.append(current)

    return visited

print(bfs(graph, 1))

#%%

def find_paths(graph, start):
    queue = [start]
    paths = {start: [start]}

    while queue != []:
        current = queue.pop(0)
        for neighbor in graph[current]:
            # Q: why is this check required?
            if neighbor not in paths:
                paths[neighbor] = paths[current] + [neighbor]
                queue.append(neighbor)

    return paths

def find_path(graph, start, end):
    paths = find_paths(graph, start)

    if end in paths:
        return paths[end]
    else:
        return None

print(find_paths(graph, 1))
print(find_path(graph, 1, 8))
print(find_path(graph, 1, 14))

#%%
import networkx as nx

G = nx.DiGraph()

G.add_node(1)
G.add_node(2)
G.add_node(3)

G.add_edge(1, 2)
G.add_edge(2, 3)

print(nx.shortest_path(G)[1][3])
# %%
