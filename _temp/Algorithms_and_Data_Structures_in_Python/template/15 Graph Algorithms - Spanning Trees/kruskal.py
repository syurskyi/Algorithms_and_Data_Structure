
c_ Vertex o..

	___ -  name
		name _ name;
		node _ N..; # !!!!
		
c_ Node o..

	___ -  height, nodeId, parentNode
		height _ height;
		nodeId _ nodeId;
		parentNode _ parentNode;
		
c_ Edge o..
	
	___ -  weight, startVertex, targetVertex
		weight _ weight;
		startVertex _ startVertex;
		targetVertex _ targetVertex;
		
	___ __cmp__ otherEdge
		r_ cmp(weight, otherEdge.weight);
		
	___ __lt__ other
		selfPriority _ weight;
		otherPriority _ other.weight;
		r_ selfPriority < otherPriority;
		
c_ DisjointSet o..

	___ -  vertexList
		vertexList _ vertexList;
		rootNodes _    # list;
		nodeCount _ 0;
		setCount _ 0;
		makeSets(vertexList);
		
	___ find node
	
		currentNode _ node;
		
		_____ currentNode.parentNode __ n.. N..:
			currentNode _ currentNode.parentNode;
			
		root _ currentNode;
		currentNode _ node;
		
		_____ currentNode __ n.. root:
			temp _ currentNode.parentNode;
			currentNode.parentNode _ root;
			currentNode _ temp;
			
		r_ root.nodeId;
	
	___ merge node1, node2
	
		index1 _ find(node1);
		index2 _ find(node2);
		
		__ index1 __ index2:
			r_;  # they are in the same set !!!!
			
		root1 _ rootNodes[index1];
		root2 _ rootNodes[index2];
		
		__ root1.height < root2.height:
			root1.parentNode _ root2;
		elif root1.height > root2.height:
			root2.parentNode _ root1;
		____
			root2.parentNode _ root1;
			root1.height _ root1.height + 1;
		
	___ makeSets vertexList
		___ v __ vertexList:
			makeSet(v);
			
	___ makeSet vertex
		node _ Node(0, l..(rootNodes),N..);
		vertex.node _ node;
		rootNodes.a..(node);
		setCount _ setCount + 1;
		nodeCount _ nodeCount + 1;
		
c_ KruskalAlgorithm o..

	___ spanningTree vertexList, edgeList
	
		disjointSet _ DisjointSet(vertexList);
		spanningTree _    # list;
		
		edgeList.sort();
		
		___ edge __ edgeList:
		
			u _ edge.startVertex;
			v _ edge.targetVertex;
			
			__ disjointSet.find(u.node) __ n.. disjointSet.find(v.node
				spanningTree.a..(edge);
				disjointSet.merge(u.node, v.node);  # !!!! dot
				
		___ edge __ spanningTree:
			print(edge.startVertex.name," - ", edge.targetVertex.name);
			
vertex1 _ Vertex("a");
vertex2 _ Vertex("b");
vertex3 _ Vertex("c");
vertex4 _ Vertex("d");
vertex5 _ Vertex("e");
vertex6 _ Vertex("f");
vertex7 _ Vertex("g");

edge1 _ Edge(2,vertex1,vertex2);
edge2 _ Edge(6,vertex1,vertex3);
edge3 _ Edge(5,vertex1,vertex5);
edge4 _ Edge(10,vertex1,vertex6);
edge5 _ Edge(3,vertex2,vertex4);
edge6 _ Edge(3,vertex2,vertex5);
edge7 _ Edge(1,vertex3,vertex4);
edge8 _ Edge(2,vertex3,vertex6);
edge9 _ Edge(4,vertex4,vertex5);
edge10 _ Edge(5,vertex4,vertex7);
edge11 _ Edge(5,vertex6,vertex7);


vertexList _    # list;
vertexList.a..(vertex1);
vertexList.a..(vertex2);
vertexList.a..(vertex3);
vertexList.a..(vertex4);
vertexList.a..(vertex5);
vertexList.a..(vertex6);
vertexList.a..(vertex7);

edgeList _    # list;
edgeList.a..(edge1);
edgeList.a..(edge2);
edgeList.a..(edge3);
edgeList.a..(edge4);
edgeList.a..(edge5);
edgeList.a..(edge6);
edgeList.a..(edge7);
edgeList.a..(edge8);
edgeList.a..(edge9);
edgeList.a..(edge10);
edgeList.a..(edge11);

algorithm _ KruskalAlgorithm();
algorithm.spanningTree(vertexList, edgeList);			
	


