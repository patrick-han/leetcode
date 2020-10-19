# Depth First Search

test_graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

# Iterative
def dfs(start_node, graph):
    stack = []
    seen = set()
    stack.append(start_node)
    while (stack):
        current = stack.pop()
        if current not in seen:
            seen.add(current)
            print(current)
        for child in graph[current]:
            if child not in seen:
                stack.append(child)

dfs('A', test_graph)

print("------")

# Recursive
def dfs2(start_node, graph):
    seen = set()
    def dfs_r(start_node, graph, seen):
        seen.add(start_node)
        print(start_node)
        for u in graph[start_node]:
            if u not in seen:
                dfs_r(u, graph, seen)
    
    dfs_r(start_node, graph, seen)

dfs2('A', test_graph)
