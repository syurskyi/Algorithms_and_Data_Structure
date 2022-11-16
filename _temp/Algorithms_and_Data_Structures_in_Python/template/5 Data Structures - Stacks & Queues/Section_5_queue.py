
#FIFO - first -> first

c_ Queue:

	___ -  
		queue _ []
		
	___ isEmpty 
		r_ queue == []
		
	___ enqueue data
		queue.append(data)
		
	___ dequeue 
		data _ queue[0]
		del queue[0]
		r_ data
		
	___ peek 
		r_ queue[0]
		
	___ sizeQueue 
		r_ len(queue)
	
queue _ Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.sizeQueue())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print(queue.sizeQueue())