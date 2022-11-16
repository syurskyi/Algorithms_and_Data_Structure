#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# reverse Solution


___ reverse(strng
    __ l..(strng) <_ 1:
      r_ strng
    r_ strng[l..(strng)-1] + reverse(strng[0:l..(strng)-1])


print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'