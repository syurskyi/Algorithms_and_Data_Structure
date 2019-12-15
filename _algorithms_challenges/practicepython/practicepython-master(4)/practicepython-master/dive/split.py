#this program is test the split functionality


li=['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']

print li

s = ';'.join(li)

print s

print s.split(';')

print s.split(';',1) #split until 1st elem

print s.split(';',2) #split until n elem
