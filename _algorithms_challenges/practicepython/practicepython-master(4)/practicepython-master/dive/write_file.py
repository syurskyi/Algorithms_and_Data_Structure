import datetime
fileobj = open('logfile.log','w') #open in write mode. creates new file if does not exist, if exist overwrites its contents


fileobj.write(str(datetime.datetime.now())+"\t logged line 1")
print file('logfile.log').read()
fileobj.close()

#open in append mode. append creates file if it does not exist. adds content to eof

fileobj2 = open('logfile.log','a') #append mode

fileobj2.write("\n"+str(datetime.datetime.now())+"\t appended line 2")
fileobj2.close()

print file('logfile.log').read()

