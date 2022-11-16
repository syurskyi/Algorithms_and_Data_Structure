#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# stringifyNumbers Solution

___ stringifyNumbers(obj
    newObj _ obj
    ___ key __ newObj:
        __ type(newObj[key]) __ int:
            newObj[key] _ str(newObj[key])
        __ type(newObj[key]) __ dict:
            newObj[key] _ stringifyNumbers(newObj[key])
    r_ newObj



obj _ {
  "num": 1,
  "test":    # list,
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

print(stringifyNumbers(obj))

{'num': '1', 
 'test':    # list, 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
}