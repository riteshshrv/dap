'''Simple implementation of Depth First Search. 'graph' is an adjacency 
	list in form of a Python Dictionary and 's' is the vertext we wish to 
	start with.'''

def dfs(graph,v):
	parent={}
	for s in v:
		if s not in parent:
			parent[s]=None
			dfs-visit(graph,v)
			
def dfs-visit(adj,s):
	for v in adj[s]:
		if v not in parent:
			parent[v]=s
			dfs-visit(adj,v)