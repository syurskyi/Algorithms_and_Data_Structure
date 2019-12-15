import os

print os.path.join("c:\\music\\ap\\", "mahadeva.mp3") #/ at the end there

print os.path.join("c:\\music\\ap", "mahadeva.mp3") #/ at the end not there but will get added by path module

#current user home directory

print os.path.expanduser('~')

#join some directory to current user home

print os.path.join( os.path.expanduser('~') , "Python")




