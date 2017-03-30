---
layout: post
title:  "FLoyd Warshall Algorithm"
categories: implementation Graph
author: "Rahul"
---
The Floyd–Warshall algorithm compares all possible paths through the graph between each pair of vertices.
It is able to do this with O(n^3) comparisons in a graph
We initialize the solution matrix same as the input graph matrix as a first step. 
Then we update the solution matrix by considering all vertices as an intermediate vertex.
The idea is to one by one pick all vertices and update all shortest paths which include the picked vertex as an intermediate vertex in the shortest path. 
When we pick vertex number k as an intermediate vertex, we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices.
For every pair (i, j) of source and destination vertices respectively, there are two possible cases.
1) k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j] as it is.
2) k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j] as dist[i][k] + dist[k][j].



```python
v=4
inf=99999
def floyd(graph):
	dist=map(lambda i:map(lambda j :j,i),graph)
	for k in range(v):
		for i in range(v):
			for j in range(v):
				dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
	printsolution(dist)
def printsolution(dist):
	Print "Following matrix shows the shortest distance\ between every pair of vertices"
	for i in range(v):
		for j in range(v):
			if dist[i][j]==inf:
				print "INF"
			else:
				print dist[i][j]
			if j==v-1:
				print ""
graph = [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
        ]
# Print the solution
floyd(graph)



```
