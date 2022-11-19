#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# collectStrings Solution

___ collectStrings(obj
    resultArr _    # list
    ___ key __ obj:
        __ type(obj[key]) __ s..:
            resultArr.a..(obj[key])
        __ type(obj[key]) __ dict:
            resultArr _ resultArr + collectStrings(obj[key])
    r_ resultArr



obj _ {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

print(collectStrings(obj)) # ['foo', 'bar', 'baz'])