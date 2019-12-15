

from sys import argv

script,username = argv
prompt='>'

print "Hi %s I am the %s script"%(username,script)

print "I would like you to ask few  questions"

print "Do you like me %s "%username

likes = raw_input(prompt)

print "Where do u live %s"%username

lives = raw_input(prompt)

print "What kind of computer do you have %s"%username

computer =  raw_input(prompt)

print """
Alright %r so you have said %r about liking me
You live at %r
you have a %r computer. Nice.
""" % (username,likes, lives, computer)
