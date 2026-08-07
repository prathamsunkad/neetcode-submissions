"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self,node, newgraph, seen_map):
        if(seen_map.get(node.val,0) == 0):
            newgraph.val = node.val
            seen_map[newgraph.val] = newgraph

        for i in node.neighbors:
            temp_val = i.val
            if(seen_map.get(temp_val,0)!=0):
                newgraph.neighbors.append(seen_map[temp_val])
            else:
                newnewgraph = Node()
                newgraph.neighbors.append(self.dfs(i,newnewgraph,seen_map))

        return newgraph
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newgraph = Node()
        seen_map = {}
        if node is None:
            return node

        return self.dfs(node, newgraph,seen_map)



        
        