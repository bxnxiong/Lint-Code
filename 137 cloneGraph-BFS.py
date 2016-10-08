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
            book = {}
            q = []
            q.append(node)
            copy = UndirectedGraphNode(node.label)
            book[node] = copy
                
            while q:
                curr = q.pop(0)
                    
                for i in curr.neighbors:
                    if i not in book:
                        copy_i = UndirectedGraphNode(i.label)
                        book[i] = copy_i
                        book[curr].neighbors.append(copy_i)
                        q.append(i)
                    else:
                        book[curr].neighbors.append(book[i])
            
            return book[node]
        else:
            return