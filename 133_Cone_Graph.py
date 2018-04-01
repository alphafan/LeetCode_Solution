"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""


# Definition for a undirected graph node
class UndirectedGraphNode:

    def __init__(self, x):
        self.label = x
        self.neighbors = []

    @staticmethod
    def clone(other):
        if other is None:
            return
        node = UndirectedGraphNode(other.label)
        node.neighbors = other.neighbors
        return node

    def __repr__(self):
        return str(self.label)


class Solution:

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return
        # Breadth First Search
        clonedNode = UndirectedGraphNode.clone(node)
        queue, visited = [clonedNode], set()
        while queue:
            node = queue.pop(0)
            if node.label not in visited:
                visited.add(node.label)
                neighbors = [UndirectedGraphNode.clone(neighbor)
                             for neighbor in node.neighbors
                             if neighbor.label not in visited]
                queue.extend(neighbors)
        return clonedNode


a, b, c, d, e, f, g = (UndirectedGraphNode(i) for i in 'abcdefg')
a.neighbors = [b, f, g]
b.neighbors = [c, g]
c.neighbors = [e, f]
d.neighbors = [f, a]
e.neighbors = []
f.neighbors = [c, b]
g.neighbors = [a]

s = Solution()
clone = s.cloneGraph(a)
assert clone is not a
for node in clone.neighbors:
    print(node, node.neighbors)













