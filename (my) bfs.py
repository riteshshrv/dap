'''Simple implementation of Breadth First Search. 'graph' is an adjacency 
	list in form of a Python Dictionary and 's' is the vertext we wish to 
	start with.'''

def bfs(graph,s):
	level={s:0}
	parent={s:None}
	i=1
	frontier=[s]
	while frontier:
		next=[]
		for u in frontier:
			for v in graph[u]:
				if v not in level:
					level[v]=i
					parent[v]=u
					next.append(v)
		# print(next,parent,i)
		frontier=next
		i+=1
