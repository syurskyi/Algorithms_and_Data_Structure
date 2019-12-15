
def smooth_weather(values):
    result = [0]*len(values)
    result[0] = values[0]
    result[-1] = values[-1]

    for i in range(len(values)-2):
        smoothed_weather = round((values[i]+values[i+1]+values[i+2])/3, 7)
        result[i+1] = smoothed_weather

    return result

values = list(map(float, input().split()))
print(*smooth_weather(values))