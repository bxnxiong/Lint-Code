# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        # write your code here
        if node:
            return self.dfs(node,{})
        else:
            return
        
    def dfs(self,node,book):
        if node in book:
            return book[node]
        else:
            new_n = UndirectedGraphNode(node.label)
            book[node] = new_n
            for i in node.neighbors:
                new_n.neighbors.append(self.dfs(i,book))
            return new_n