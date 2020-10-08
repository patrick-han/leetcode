class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.dfs(graph, [0], 0, res) # Start at node 0, with an initial path of just node 0
        
        return res
        
        
    def dfs(self, graph: List[List[int]], cur_res: List[int], cur_node: int, res: List[List[int]]) -> None:
        if cur_node == len(graph) - 1: # If we've reached the last node, then just add that path to the result list
            res.append(list(cur_res))
        
        for node in graph[cur_node]: # Else, we need to look at the current node be visited's adjacent nodes
            cur_res.append(node) # Add that adjacent node to the current node's path 
            self.dfs(graph, cur_res, node, res) # Pass it back in
            cur_res.pop() # Pop because we need to build passed cur_res's for other adjacent nodes