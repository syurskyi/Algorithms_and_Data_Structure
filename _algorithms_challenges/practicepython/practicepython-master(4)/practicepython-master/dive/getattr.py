import apihelper
import types
#working with getattr in built in data types
li = ["larry" ,"curly"]

#normal pop method
print li.pop

#getting reference to pop  method using the getattr function
print getattr(li , "pop")



#getting the reference and appending the element using the getattr function

print li

getattr(li, "append")("newly appended variable")

print li

#working with getattr in modules

print apihelper

print apihelper.info

print getattr(apihelper, "info")

#check whether the info method is callable
print callable(getattr(apihelper, "info"))
#print callable(getattr(apihelper, "wrongmethod"))

print types.FunctionType

print type(callable(getattr(apihelper,"info")))
