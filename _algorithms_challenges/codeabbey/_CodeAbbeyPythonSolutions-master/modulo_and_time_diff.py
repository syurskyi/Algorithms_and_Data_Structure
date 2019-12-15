amount_values = int(input())
results = []

def get_time_diff(d1, h1, m1, s1, d2, h2, m2, s2):
    day_in_seconds = 24*60*60
    hour_in_seconds = 60*60
    minute_in_seconds = 60

    time2_in_seconds = (d2*day_in_seconds)+(h2*hour_in_seconds)+(m2*minute_in_seconds)+s2
    time1_in_seconds = (d1*day_in_seconds)+(h1*hour_in_seconds)+(m1*minute_in_seconds)+s1

    time_diff_in_seconds = time2_in_seconds - time1_in_seconds
    time_diff_day = (time_diff_in_seconds)//(day_in_seconds)

    time_diff_in_seconds -= (day_in_seconds* time_diff_day)
    time_diff_hour = (time_diff_in_seconds)//(hour_in_seconds)

    time_diff_in_seconds -= (hour_in_seconds* time_diff_hour)
    time_diff_minute = (time_diff_in_seconds)//(minute_in_seconds)

    time_diff_seconds = time_diff_in_seconds - (minute_in_seconds*time_diff_minute)

    return "("+str(time_diff_day)+" "+str(time_diff_hour) +" "+ str(time_diff_minute)+" "+ str(time_diff_seconds)+")"

for i in range(amount_values):
    d1,h1,m1,s1,d2,h2,m2,s2 = map(int,input().split())
    results.append(get_time_diff(d1,h1,m1,s1, d2, h2, m2, s2))

print(*results)