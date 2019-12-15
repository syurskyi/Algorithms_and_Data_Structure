# my_name = "praveen"
# my_age = 25
# my_weight = 55
# my_height = 172
# my_eyes = 'Brown'
# my_teeth = 'White'
# my_hair = 'Brown'
#
# print "lets talk about %s" % my_name
# print "he is %d inches tall." % my_height
# print "he is %d kg heavy " % my_weight
#
# print "he has got %s eyes and %s hair" %(my_eyes,my_hair)
# print "his teeth is usually %s depending on the coffee " %my_teeth
#
# #this line is tricky, try to get it exactly right
# print " If i add %d ,%d and %d I get %d "%(my_age, my_height, my_weight, my_age + my_height + my_weight)
name = "praveen"
age = 25
weight = 55
height = 172
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

cm_height = height * 2.54
pound_weight = weight *2.20462
print "lets talk about %s " % name
print "he is %d inches tall." % height
print "he is %d kg heavy " % weight

print "he has got %s eyes and %s hair" %(eyes,hair)
print "his teeth is usually %s depending on the coffee " %teeth

#this line is tricky, try to get it exactly right
print " If i add %d ,%d and %d I get %d "%(age, height, weight, age + height + weight)

print "pound weight %f" % pound_weight
print "height cm %f" % cm_height
print "height cm %f" % round(cm_height) #check round
