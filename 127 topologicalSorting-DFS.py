# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        
        color = {u:'w' for u in graph}
        
        cycle = False
        
        result = []
        for u in graph:
            self.dfs(u,color,result,cycle)
        
        result.reverse()
        if not cycle:
            return result
        else:
            return []
        
    def dfs(self,u,color,result,cycle):
        if color[u] == 'w':
            color[u] = 'g'
            for i in u.neighbors:
                self.dfs(i,color,result,cycle)
            result.append(u)
            color[u] = 'b'
                
        if color[u] == 'g':
            cycle = True
            