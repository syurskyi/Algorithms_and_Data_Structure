import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Euclidean distance - we can omit the square-root function
def distance(p, q):
    return math.sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y))


# it has quadratic running time so we want to do better
def brute_force(sub_array):
    # initialize the min_distance to INF
    min_distance = float('inf')

    # we have to calculate the distance between every single point
    # we make sure that do not consider the same points multiple times
    # d(a,b) = d(b,a)
    for i in range(len(sub_array) - 1):
        for j in range(i + 1, len(sub_array)):
            actual_distance = distance(sub_array[i], sub_array[j])
            if actual_distance < min_distance:
                min_distance = actual_distance

    return min_distance


def get_strip_delta(strip_points, delta):
    min_distance = delta
    n = len(strip_points)

    # in worst case len(strip_point) = N
    for i in range(n):
        j = i + 1
        # a geometric packing argument shows that this loop iterates at most 7 times
        # THIS IS WHY WE HAVE SORTED THE POINTS BASED ON Y COORDINATE
        while j < n and (strip_points[j].y - strip_points[i].y) < min_distance:
            min_distance = distance(strip_points[j], strip_points[i])
            j = j + 1

    return min_distance


def closest_pairs_algorithm(list_sorted_x, list_sorted_y, num_of_items):
    # when the number of items smaller than 3 then we use brute-force
    # base case
    if num_of_items <= 5:
        return brute_force(list_sorted_x)

    middle_index = num_of_items // 2
    middle_item = list_sorted_x[middle_index]

    # DIVIDE PHASE
    delta_left = closest_pairs_algorithm(list_sorted_x[:middle_index], list_sorted_y, middle_index)
    delta_right = closest_pairs_algorithm(list_sorted_x[middle_index:], list_sorted_y, num_of_items - middle_index)

    delta = min(delta_left, delta_right)

    # CONQUER PHASE - usually this is where the magic happens
    strip_points = []

    for i in range(num_of_items):
        if abs(list_sorted_y[i].x - middle_item.x) < delta:
            strip_points.append(list_sorted_y[i])

    strip_delta = get_strip_delta(strip_points, delta)

    return min(strip_delta, delta)


def run(list1, list2):
    list1.sort(key=lambda point: point.x)
    list2.sort(key=lambda point: point.y)
    return closest_pairs_algorithm(list1, list2, len(list1))


if __name__ == '__main__':
    points = [Point(1, 1), Point(4, 2), Point(10, 10), Point(1, 2), Point(5, 3)]

    l1 = list(points)
    l2 = list(points)

    print(run(l1, l2))
