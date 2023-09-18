class Solution:
    def minCostConnectPoints(self, points):
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance, i, j))

        edges.sort()  
        parent = list(range(n))
        min_cost = 0

        for distance, i, j in edges:
            if find(i) != find(j):
                union(i, j) #to take the union
                
                min_cost += distance

        return min_cost
