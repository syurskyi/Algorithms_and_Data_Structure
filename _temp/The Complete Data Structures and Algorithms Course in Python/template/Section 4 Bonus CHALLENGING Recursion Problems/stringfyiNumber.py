#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# stringifyNumbers Solution

___ stringifyNumbers(obj
    newObj _ obj
    ___ key __ newObj:
        __ type(newObj[key]) __ i..:
            newObj[key] _ s..(newObj[key])
        __ type(newObj[key]) __ dict:
            newObj[key] _ stringifyNumbers(newObj[key])
    r_ newObj



obj _ {
  "num": 1,
  "test":    # list,
  "data": {
    "val": 4,
    "info": {
      "isRight": T..,
      "random": 66
    }
  }
}

print(stringifyNumbers(obj))

{'num': '1', 
 'test':    # list, 
 'data': {'val': '4', 
          'info': {'isRight': T.., 'random': '66'}
          }
}