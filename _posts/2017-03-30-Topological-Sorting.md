---
layout: post
title:  "Topological Sorting"
categories: implementation Graph
author: "Rahul"
---
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, 
vertex u comes before v in the ordering. 
Topological Sorting for a graph is not possible if the graph is not a DAG.

```python
from collections import defaultdict
#This class represents a directed graph 
#using adjacency list trepresentation
class Graph:
	def __init__(self,vertices):#Constructor
		#Dictionary containing adjacency list
		self.graph=defaultdict(list)
		#No of vertices
		self.V=vertices
	#Function to add edge
	def addedge(self,u,v):
		self.graph[u].append(v)
	#Recursive function used by topologicalsort
	def TSortuse(self,v,visited,stack):
		#Mark thw current node as visited
		visited[v]=True
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.TSortuse(i,visited,stack)
		#push current vertex to stack
		stack.insert(0,v)
	#function for topological sorting of DAG
	def topologicalsort(self):
		#Mark all the vertices as not visited
		visited=[False]*self.V
		stack=[]
		for i in range(self.V):
			if visited[i]==False:
				self.TSortuse(i,visited,stack)
		print stack
#Driver Program to test above class
g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
 
print "Following is a Topological Sort of the given graph"
g.topologicalSort()



```
