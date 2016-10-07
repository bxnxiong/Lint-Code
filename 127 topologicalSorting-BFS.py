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
        outDegree = {}
        
        for u in graph:
            outDegree[u] = u.neighbors
        
        inDegree = {u:0 for u in graph}
        
        for u in graph:
            for i in u.neighbors:
                inDegree[i] += 1
        
        q = []
        for i in inDegree:
            if inDegree[i] == 0:
                q.append(i)
        
        result = []
        
        while q:
            node = q.pop(0)
            result.append(node)
            
            for i in outDegree[node]:
                inDegree[i] -= 1
                
                if inDegree[i] == 0:
                    q.append(i)
        #print [x.label for x in result]
        if len(result) == len(graph):
            return result
        else:
            return
        