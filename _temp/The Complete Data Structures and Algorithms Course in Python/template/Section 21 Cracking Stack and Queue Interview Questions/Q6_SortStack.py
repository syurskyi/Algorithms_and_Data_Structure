#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Sort a stack with the smallest on top using only a single temporary stack.

___ sort_stack(stack
  previous _ stack.pop()
  current _ stack.pop()
  temp _ Stack()
  _____ current:
    __ previous < current:
      temp.push(previous)
      previous _ current
      current _ stack.pop()
    ____
      temp.push(current)
      current _ stack.pop()
    __ current __ N.. and previous: temp.push(previous)
       
  sorted _ True
  previous _ temp.pop()
  current _ temp.pop()
  _____ current:
    __ previous > current:
      stack.push(previous)
      previous _ current
      current _ temp.pop()
    ____
      stack.push(current)
      current _ temp.pop()
      sorted _ False
    __ current __ N.. and previous: stack.push(previous)
  __ sorted: r_ stack
  ____ r_ sort_stack(stack)

c_ Stack(
  ___ -
    top _ N..
  
  ___ __str__
    r_ str(top)
  
  ___ push item
    top _ current(item, top)
  
  ___ pop
    __ n.. top:
      r_ N..
    item _ top
    top _ top.next
    r_ item.data

c_ current(
  ___ -  data_None, next_None
    data, next _ data, next
  
  ___ __str__
    r_ str  and data) + ',' + str  and next)

import unittest

c_ Test(unittest.TestCase
  ___ test_sort_stack
    assertEqual(str(sort_stack(Stack())), "None")
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
    assertEqual(str(stack), "60,50,90,20,80,40,70,30,10,None")
    assertEqual(str(sort_stack(stack)), "10,20,30,40,50,60,70,80,90,None")

unittest.main()