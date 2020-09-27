class Solution:
'''
Problem Name:  Evaluate Division
Author: Ayushi Rawat
Date: 27-09-2020
'''
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        for i, var in enumerate(equations):
            if var[0] not in adj:
                adj[var[0]] = []
            if var[1] not in adj:
                adj[var[1]] = []
                
            adj[var[0]].append([var[1], values[i]])
            adj[var[1]].append([var[0], 1.0/values[i]])
         
        output = []
        
        for q in queries:
            if (q[0] not in adj) or (q[1] not in adj):
                output.append(-1.0)
            elif(q[0] == q[1]):
                output.append(1.0)
            else:
                output.append(self.helper(adj, q[0], q[1]))
                
        return output
    
    def helper(self, graph, start, end):
        queue = [(start, 1.0)]
        
        seen = set()
        
        while queue:
            curr, val = queue.pop(0)
            seen.add(curr)

            if curr == end:
                return val

            for neighbor in graph[curr]:
                next, weight = neighbor
                
                if next not in seen:
                    queue.append((next, val*weight))
        return -1.0