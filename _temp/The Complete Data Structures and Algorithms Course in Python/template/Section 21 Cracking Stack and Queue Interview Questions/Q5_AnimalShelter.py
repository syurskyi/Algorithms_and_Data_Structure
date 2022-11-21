# #   Created by Elshad Karimov on 02/06/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# # Implement a cat and dog queue for an animal shelter.
#
# c_ AnimalShelter
#   ___ -
#     cats _    # list
#     dogs _    # list
#
#   ___ enqueue animal, type
#     __ ? __ 'Cat'
#       ?.a.. ?
#     ____
#       ?.a.. ?
#
#   ___ dequeueCat
#     __ l.. ? __ 0
#       r_ N..
#     ____
#       c.. _ ?.p.. 0
#       r_ ?
#
#   ___ dequeueDog
#     __ l.. ? __ 0
#       r_ N..
#     ____
#       d.. _ ?.p.. 0
#       r_ ?
#
#   ___ dequeueAny
#     __ l.. ? __ 0
#       result _ ?.p.. 0
#     ____
#       result _ ?.p.. 0)
#     r_ ?
#
# customQueue _ AnimalShelter()
# customQueue.enqueue('Cat1', 'Cat')
# customQueue.enqueue('Cat2', 'Cat')
# customQueue.enqueue('Dog1', 'Dog')
# customQueue.enqueue('Cat3', 'Cat')
# customQueue.enqueue('Dog2', 'Dog')
# print(customQueue.dequeueAny())
