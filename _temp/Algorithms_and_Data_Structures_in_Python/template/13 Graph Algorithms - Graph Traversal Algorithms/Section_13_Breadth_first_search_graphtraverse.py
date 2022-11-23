
c_ Node o..

	___ -  name
		name _ name;
		adjacencyList _    # list;
		visited _ F..;
		predecessor _ N..;
		
c_ BreadthFirstSearch o..

	___ bfs startNode
	
		queue _    # list;
		queue.a..(startNode);
		startNode.visited _ T..;
		
		# BFS -> queue      DFS --> stack BUT usually we implement it with 001_recursion !!!
		_____ queue:
		
			actualNode _ queue.p.. 0);
			print("%s " _ actualNode.name);
			
			___ n __ actualNode.adjacencyList:
				__ n.. n.visited:
					n.visited _ T..;
					queue.a..(n);
					
node1 _ Node("A");
node2 _ Node("B");
node3 _ Node("C");
node4 _ Node("D");
node5 _ Node("E");

node1.adjacencyList.a..(node2);
node1.adjacencyList.a..(node3);
node2.adjacencyList.a..(node4);
node4.adjacencyList.a..(node5);

bfs _ BreadthFirstSearch();
bfs.bfs(node1);