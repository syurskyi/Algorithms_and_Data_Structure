f = open("/home/praveen/Music/Anandam.mp3","rb")

print f

print f.mode


print f.name


print f.tell()

f.seek(-128,2)

print f.tell()

tagData = f.read(128)

print tagData

f.tell()

print f
print f.closed
f.close()
print f
print f.closed

f.seek(0)
