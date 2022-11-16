
c_ Node o..

	___ -  name
		name _ name;
		adjacencyList _ [];
		visited _ False;
		predecessor _ N..;
		
c_ BreadthFirstSearch o..

	___ bfs startNode
	
		queue _ [];
		queue.append(startNode);
		startNode.visited _ True;
		
		# BFS -> queue      DFS --> stack BUT usually we implement it with 001_recursion !!!
		_____ queue:
		
			actualNode _ queue.pop(0);
			print("%s " % actualNode.name);
			
			___ n __ actualNode.adjacencyList:
				__ n.. n.visited:
					n.visited _ True;
					queue.append(n);
					
node1 _ Node("A");
node2 _ Node("B");
node3 _ Node("C");
node4 _ Node("D");
node5 _ Node("E");

node1.adjacencyList.append(node2);
node1.adjacencyList.append(node3);
node2.adjacencyList.append(node4);
node4.adjacencyList.append(node5);

bfs _ BreadthFirstSearch();
bfs.bfs(node1);