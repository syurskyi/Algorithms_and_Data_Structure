import types

print types.FunctionType

#print FunctionType gives error


from types import FunctionType
print FunctionType #using from import we can use wihout namespace
print types

print dir(types) #types module contains only attributes for each python object type
