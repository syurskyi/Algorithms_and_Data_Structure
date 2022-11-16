#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# reverse Solution


___ reverse(strng
    __ len(strng) <_ 1:
      r_ strng
    r_ strng[len(strng)-1] + reverse(strng[0:len(strng)-1])


print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'