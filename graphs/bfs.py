# Breadth First Search

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

def bfs(start_node, graph):
    queue = []
    seen = set()
    queue.insert(0, start_node)
    while (queue):
        current = queue.pop()
        if current not in seen:
            seen.add(current)
            print(current)
        for child in graph[current]:
            if child not in seen:
                queue.insert(0, child)

bfs('A', test_graph)