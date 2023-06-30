#!/usr/bin/env python
# coding: utf-8

# # Route BetweenNodes Test

# In[ ]:


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex] = edge
    
    def checkRoute(self, startNode, endNode):
        visited = []
        queue = [startNode]
        path = []
        if startNode == endNode:
            return [startNode]
        while queue:
            deVertex = queue.pop(0)
            path.append(deVertex)
            if deVertex not in visited:
                visited.append(deVertex)
            if deVertex == endNode:
                return path
            adjacentVertices = self.gdict[deVertex]
            for adjacentVertex in adjacentVertices:
                if adjacentVertex not in visited:
                    queue.append(adjacentVertex)
        return None

# Creating a graph object
customDict = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": ["d", "f"],
    "f": ["g"],
    "g": ["h"],
    "h": ["i"],
    "i": ["j"],
    "j": []
}

g = Graph(customDict)
print(g.checkRoute("a", "j"))

