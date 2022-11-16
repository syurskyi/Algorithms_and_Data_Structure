#
# #FIFO - first -> first
#
# c_ Queue
#
# 	___ -
# 		queue _    # list
#
# 	___ isEmpty
# 		r_ queue __    # list
#
# 	___ enqueue data
# 		?.a.. ?
#
# 	___ dequeue
# 		data _ ? 0
# 		d.. ? 0
# 		r_ ?
#
# 	___ peek
# 		r_ ? 0
#
# 	___ sizeQueue
# 		r_ l.. ?
#
# queue _ Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# print(queue.sizeQueue())
# print("Dequeue: ", queue.dequeue())
# print("Dequeue: ", queue.dequeue())
# print(queue.sizeQueue())