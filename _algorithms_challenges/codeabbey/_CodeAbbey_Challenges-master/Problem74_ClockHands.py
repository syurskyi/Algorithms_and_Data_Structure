import math

infile = open("prob74.txt")
infile.readline()
data = infile.readline().split()
# convert 24-hr to 12hr
times = [] # format (hr,min) int
for time in data:
    time = time.split(":")
    times.append((int(time[0])%12,int(time[1])))
      
# find angle

for item in times:
    hrAngle = int(item[0])*30 + 30*(int(item[1])/60)
    xhr = 10+6*math.sin(hrAngle*math.pi/180) # convert degree to radian
    yhr = 10+6*math.cos(hrAngle*math.pi/180)

    minAngle = int(item[1])*6
    xmin = 10+9*math.sin(minAngle*math.pi/180)
    ymin = 10+9*math.cos(minAngle*math.pi/180)

    print("{:.7f} {:.7f} {:.7f} {:.7f}".format(xhr,yhr,xmin,ymin),end=" ")
