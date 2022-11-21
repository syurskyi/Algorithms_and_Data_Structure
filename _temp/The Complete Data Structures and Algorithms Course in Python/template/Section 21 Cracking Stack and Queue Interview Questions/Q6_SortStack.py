#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Sort a stack with the smallest on top using only a single temporary stack.

___ sort_stack(stack
  previous _ stack.p.. 
  current _ stack.p.. 
  temp _ Stack()
  _____ current:
    __ previous < current:
      ?.push(previous)
      p.. _ ?
      current _ stack.p.. 
    ____
      ?.push(current)
      current _ stack.p.. 
    __ c.. __ N.. ___ previous: ?.push(previous)
       
  s.. _ T..
  previous _ ?.p.. 
  current _ ?.p.. 
  _____ current:
    __ previous > current:
      stack.push(previous)
      p.. _ ?
      current _ ?.p.. 
    ____
      stack.push(current)
      current _ ?.p.. 
      s.. _ F..
    __ c.. __ N.. ___ previous: stack.push(previous)
  __ s..: r_ stack
  ____ r_ sort_stack(stack)

c_ Stack(
  ___ -
    top _ N..
  
  ___ __str__
    r_ s..(top)
  
  ___ push item
    top _ current(item, top)
  
  ___ pop
    __ n.. top:
      r_ N..
    item _ top
    top _ top.n..
    r_ item.data

c_ current(
  ___ -  data_None, next_None
    data, next _ data, next
  
  ___ __str__
    r_ s..  ___ data) + ',' + s..  ___ next)

______ unittest

c_ Test(unittest.TestCase
  ___ test_sort_stack
    assertEqual(s..(sort_stack(Stack())), "None")
    stack _ Stack()
    stack.push(10)
    stack.push(30)
    stack.push(70)
    stack.push(40)
    stack.push(80)
    stack.push(20)
    stack.push(90)
    stack.push(50)
    stack.push(60)
    assertEqual(s..(stack), "60,50,90,20,80,40,70,30,10,None")
    assertEqual(s..(sort_stack(stack)), "10,20,30,40,50,60,70,80,90,None")

unittest.main()