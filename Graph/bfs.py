def bfs(graph, start_node):
	visited = set([start_node])
	queue = deque([start_node])
	traversal_order = []
	
	while queue:
		current_node = queue.popLeft()
		traversal_order.append(current_node)
		
		for neighbour in graph.get(current_node, []):
			if neighbour not in visited:
				visited.add(neighbour)
				queue.append(neighbour)
	return traversal_order

# graph.get(val,default_val) -> gets you all of the values associated with val. If there are none, to avoid an error we use default_val to return.
eg. graph = {
		'A': {'B','C'}
	}
graph.get('A',[]) -> will give me {'B','C'} and if we there is no value then the default value returned would be []
