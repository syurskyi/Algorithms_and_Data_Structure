#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Implement a cat and dog queue for an animal shelter.

c_ AnimalShelter(
  ___ -  
    cats _    # list
    dogs _    # list
  
  ___ enqueue animal, type
    __ type __ 'Cat':
      cats.a..(animal)
    ____
      dogs.a..(animal)
    
  ___ dequeueCat 
    __ l..(cats) __ 0:
      r_ N..
    ____
      cat _ cats.pop(0)
      r_ cat
  
  ___ dequeueDog 
    __ l..(dogs) __ 0:
      r_ N..
    ____
      dog _ dogs.pop(0)
      r_ dog
  
  ___ dequeueAny 
    __ l..(cats) __ 0:
      result _ dogs.pop(0)
    ____
      result _ cats.pop(0)
    r_ result

customQueue _ AnimalShelter()
customQueue.enqueue('Cat1', 'Cat')
customQueue.enqueue('Cat2', 'Cat')
customQueue.enqueue('Dog1', 'Dog')
customQueue.enqueue('Cat3', 'Cat')
customQueue.enqueue('Dog2', 'Dog')
print(customQueue.dequeueAny())
