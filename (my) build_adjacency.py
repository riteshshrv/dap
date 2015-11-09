''' Create adjacency matrix and adjacency list from given edge list
4		# nodes / vertices
5    	# paths
1 2		# edge list follows
2 4
3 1
3 4
4 2
'''

nodes=int(input())
paths=int(input())


# Adjacency Matrix
adj=[[0 for i in range(nodes)] for i in range(nodes)]
for i in range(paths):
	x,y=[int(x) for x in input().split()]
	adj[x-1][y-1]=1

''' Output:	adj=	[[0, 1, 0, 0],
					 [0, 0, 1, 1],
				 	 [1, 0, 0, 1],
				 	 [0, 1, 0, 0]]						'''


# Adjacency list ------ 1
adj={}
for i in range(paths):
	x,y=input().split()
	if x in adj:
		adj[x].append(y)
	else:
		adj[x]=[y]

''' Output: adj=	{'4': ['2'], 
					 '2': ['4'], 
					 '1': ['2'], 
					 '3': ['1', '4']}					'''


# Adjacency list ------ 2
from collections import defaultdict
adj=defaultdict(list)
for i in range(paths):
	x,y=input().split()
	adj[x].append(y)

''' Output: adj=	defaultdict(<class 'list'>, 
								{'4': ['2'], 
								 '2': ['4'],
								 '1': ['2'], 
								 '3': ['1', '4']})		'''