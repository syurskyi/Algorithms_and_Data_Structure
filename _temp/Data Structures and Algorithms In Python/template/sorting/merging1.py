# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

#a[low1]...a[up1] and a[low2]...a[up2] merged to temp[low1]..temp[up2]
___ merge(a,temp,low1,up1,low2,up2
      i _ low1
      j _ low2
      k _ low1
           
      _____ i <_ up1 and j <_ up2:
          __ a[i] <_ a[j]:
              temp[k] _ a[i]
              i+_1
          ____
              temp[k] _ a[j]
              j+_1
          k+_1
        
      _____ i <_ up1:
          temp[k] _ a[i]
          i+_1
          k+_1
      
      _____ j <_ up2:
          temp[k] _ a[j]
          j+_1
          k+_1

###########################################

a _ [1,2,4,6,  3,5,6,7,13,19]

temp_[N..]*l..(a)

merge(a,temp,0,3,4,9)

print("Merged list temp is : ");
print(temp)            


##########################################
