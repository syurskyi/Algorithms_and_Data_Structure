# #   Created by Elshad Karimov on 02/06/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# # Sort a stack with the smallest on top using only a single temporary stack.
#
# ___ sort_stack stack
#   previous _ ?.p..
#   current _ ?.p..
#   temp _ ?
#   _____ ?
#     __ ? < c..
#       ?.p.. p..
#       p.. _ ?
#       c.. _ ?.p..
#     ____
#       ?.p.. c..
#       c.. _ ?.p..
#     __ c.. __ N.. ___ p.. ?.p.. p..
#
#   s.. _ T..
#   previous _ ?.p..
#   current _ ?.p..
#   _____ ?
#     __ ? > c..
#       ?.p.. p..
#       p.. _ ?
#       c.. _ ?.p..
#     ____
#       ?.p.. ?
#       c.. _ ?.p..
#       s.. _ F..
#     __ c.. __ N.. ___ p.. ?.p.. p.
#   __ s..: r_ ?
#   ____ r_ s.. ?
#
# c_ Stack
#   ___ -
#     top _ N..
#
#   ___ -s
#     r_ s.. ?
#
#   ___ push item
#     top _ c... ? ?
#
#   ___ pop
#     __ n.. top
#       r_ N..
#     item _ ?
#     t.. _ ?.n..
#     r_ ?.d..
#
# c_ current
#   ___ -  data_N.. next_N..
#     ? ? _ ? ?
#
#   ___ -s
#     r_ s..  ___ data + ',' + s..  ___ ?
#
# ______ unittest
#
# c_ Test(unittest.TestCase
#   ___ test_sort_stack
#     assertEqual(s..(sort_stack(Stack())), "None")
#     stack _ Stack()
#     stack.push(10)
#     stack.push(30)
#     stack.push(70)
#     stack.push(40)
#     stack.push(80)
#     stack.push(20)
#     stack.push(90)
#     stack.push(50)
#     stack.push(60)
#     assertEqual(s..(stack), "60,50,90,20,80,40,70,30,10,None")
#     assertEqual(s..(sort_stack(stack)), "10,20,30,40,50,60,70,80,90,None")
#
# unittest.main()