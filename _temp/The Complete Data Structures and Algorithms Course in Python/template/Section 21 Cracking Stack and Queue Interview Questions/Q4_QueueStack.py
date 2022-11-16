#   Created by Elshad Karimov on 04/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Implement a queue using two stacks.

c_ Stack(
  ___ -  
    list _    # list
  
  ___ __len__ 
    r_ l..(list)
  
  ___ push item
    list.a..(item)
  
  ___ pop 
    __ l..(list) __ 0:
      r_ N..
    r_ list.p.. 

c_ QueueviaStack(
  ___ -  
    inStack _ Stack()
    outStack _ Stack()
  
  ___ enqueue item
    inStack.push(item)
  
  ___ dequeue 
    _____ l..(inStack
      outStack.push(inStack.p.. ))
    result _ outStack.p.. 
    _____ l..(outStack
      inStack.push(outStack.p.. ))
    r_ result
  

customQueue _ QueueviaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
customQueue.enqueue(4)
print(customQueue.dequeue())