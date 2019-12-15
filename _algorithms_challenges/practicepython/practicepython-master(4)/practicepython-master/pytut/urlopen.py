import urllib

file_object = urllib.urlopen("http://www.induze.com")

data = file_object.read();

file_object.close();
print data
