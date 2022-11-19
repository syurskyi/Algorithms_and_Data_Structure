import sys;
import heapq;

c_ Edge o..

	___ -  weight, startVertex, targetVertex
		weight _ weight;
		startVertex _ startVertex;
		targetVertex _ targetVertex;
		
c_ Node o..

	___ -  name
		name _ name;
		visited _ F..;
		predecessor _ N..;
		adjacenciesList _    # list;
		minDistance _ sys.maxsize;
		
	___ __cmp__ otherVertex
		r_ cmp(minDistance, otherVertex.minDistance);
		
	___ __lt__ other
		selfPriority _ minDistance;
		otherPriority _ other.minDistance;
		r_ selfPriority < otherPriority;

c_ Algorithm o..

	___ calculateShortestPath vertexList, startVertex
	
		q _    # list;
		startVertex.minDistance _ 0;
		heapq.heappush(q, startVertex);
		
		_____ q:
		
			actualVertex _ heapq.heappop(q);
			
			___ edge __ actualVertex.adjacenciesList:
				u _ edge.startVertex;
				v _ edge.targetVertex;
				newDistance _ u.minDistance + edge.weight;
				
				__ newDistance < v.minDistance:
					v.predecessor _ u;
					v.minDistance _ newDistance;
					heapq.heappush(q, v);
					
	___ getShortestPathTo targetVertex
		print("Shortest path to vertex is: ", targetVertex.minDistance);
		
		node _ targetVertex;
		
		_____ node __ n.. N..
			print("%s " % node.name);
			node _ node.predecessor;
			
node1 _ Node("A");
node2 _ Node("B");
node3 _ Node("C");
node4 _ Node("D");
node5 _ Node("E");
node6 _ Node("F");
node7 _ Node("G");
node8 _ Node("H");

edge1 _ Edge(5,node1,node2);
edge2 _ Edge(8,node1,node8);
edge3 _ Edge(9,node1,node5);
edge4 _ Edge(15,node2,node4);
edge5 _ Edge(12,node2,node3);
edge6 _ Edge(4,node2,node8);
edge7 _ Edge(7,node8,node3);
edge8 _ Edge(6,node8,node6);
edge9 _ Edge(5,node5,node8);
edge10 _ Edge(4,node5,node6);
edge11 _ Edge(20,node5,node7);
edge12 _ Edge(1,node6,node3);
edge13 _ Edge(13,node6,node7);
edge14 _ Edge(3,node3,node4);
edge15 _ Edge(11,node3,node7);
edge16 _ Edge(9,node4,node7);

node1.adjacenciesList.a..(edge1);
node1.adjacenciesList.a..(edge2);
node1.adjacenciesList.a..(edge3);
node2.adjacenciesList.a..(edge4);
node2.adjacenciesList.a..(edge5);
node2.adjacenciesList.a..(edge6);
node8.adjacenciesList.a..(edge7);
node8.adjacenciesList.a..(edge8);
node5.adjacenciesList.a..(edge9);
node5.adjacenciesList.a..(edge10);
node5.adjacenciesList.a..(edge11);
node6.adjacenciesList.a..(edge12);
node6.adjacenciesList.a..(edge13);
node3.adjacenciesList.a..(edge14);
node3.adjacenciesList.a..(edge15);
node4.adjacenciesList.a..(edge16);


vertexList _ (node1,node2,node3, node4, node5, node6, node7, node8);

algorithm _ Algorithm();
algorithm.calculateShortestPath(vertexList, node1);
algorithm.getShortestPathTo(node4);