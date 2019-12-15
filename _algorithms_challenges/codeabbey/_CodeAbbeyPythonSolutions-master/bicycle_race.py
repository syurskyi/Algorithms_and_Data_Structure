amount_values = int(input())
results = []

def get_meeting_point(distance, racer1_speed, racer2_speed):
    return (distance/(racer1_speed+racer2_speed)*racer1_speed)


for i in range(amount_values):
    distance, racer1_speed, racer2_speed = map(int, input().split())
    results.append(get_meeting_point(distance, racer1_speed, racer2_speed))

print(*results)