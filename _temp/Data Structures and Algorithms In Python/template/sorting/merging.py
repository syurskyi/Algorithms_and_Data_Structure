# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

___ merge(a1,a2,temp
      i _ 0
      j _ 0
      k _ 0
      n1_len(a1)
      n2_len(a2)
      
      _____ i <_ n1-1 ___ j <_ n2-1:
          __ a1[i] < a2[j]:
              temp[k] _ a1[i]
              i+_1
          ____
              temp[k] _ a2[j]
              j+_1
          k+_1
        
      # copy remaining elements of a1, list a2 finished
      _____ i <_ n1-1:
          temp[k] _ a1[i]
          i+_1
          k+_1
            
      # copy remaining elements of a2, list a1 finished
      _____ j <_ n2-1:
          temp[k] _ a2[j]
          j+_1
          k+_1

          
#####################################################################
n1 _ int(input("Enter the number of elements in list a1 : "))
print("Enter elements in sorted order : " );
a1 _ [N..]*n1
___ i __ r..(n1
    a1[i] _ int(input("Enter element : "))

n2 _ int(input("Enter the number of elements in list a2 : "))
print("Enter elements in sorted order : " );
a2 _ [N..]*n2
___ i __ r..(n2
    a2[i] _ int(input("Enter element : "))

temp_[N..]*(n1+n2)

merge(a1,a2,temp)

print("Merged list temp is : ");
print(temp)            

#####################################################################
