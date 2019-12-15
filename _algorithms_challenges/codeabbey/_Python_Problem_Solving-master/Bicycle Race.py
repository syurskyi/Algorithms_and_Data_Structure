# Distance =Speed * time
# 20 1 2
# As we have to calculate the distance of the first car travelled before the meet
# Here the time was not give and is common among both the cycle A and Cycle B
# dist(20) can be given as 20 = Dist(A) + Dist(B)
# according to the distance formula the above equation can be written as
# 20 = speed(A)*t + speed(B)*t i.e 20 = 1*t + 2*t
# 20 = t(1+2) -> t = 20 /(1+2) t = 6.6667
#to find the distance travelled by cycle A substitute the time travelled into Dist(A)
# thus dist(A) = 1 * 6.667
for i in range(int(input())):
    res = 0
    data = list(map(float,input().split()))
    s,a,b = data
    res = s/(a+b)
    print(res * a,end=' ')