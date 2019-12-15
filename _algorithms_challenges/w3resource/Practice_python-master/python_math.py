import math
import cmath


# 1
def degree_to_radian(degree):
    """Converts a given degree to a radian. """
    radian = degree * (math.pi / 180)
    return round(radian, 4)

# print(degree_to_radian(30))


# 2
def radian_to_degree(radian):
    """ converts radian to degrees """
    degree = (radian * 180) / math.pi
    return round(degree, 4)

# print(radian_to_degree(.52))


# 3
def trapezoid(height, base1, base2):
    """ Caculates the area of a trapezoid """
    if base1 <= base2:
        area = (base1 * height) + ((base2 - base1) * height / 2)
    else:
        area = (base2 *  height) + ((base1 - base2) * height / 2)
    return area

# print(trapezoid(5, 6, 3))


# 4
def parallelogram(height, length):
    """ Caculates the area of parallelogram """
    return height * length

# print(parallelogram(5, 6))
# 5
class Cylinder:
    radius = int(input("Radius of Cylinder: "))
    height = int(input("Height: "))

    def volume(self):
        """ caculates the volume of cylinder """
        return round((math.pi * (self.radius**2)) * self.height, 2)

    def surface_area(self):
        """ caculates the surface area of cylinder """
        return round((math.pi * self.radius * 2 * self.height)
                     + (math.pi * (self.radius**2) * 2), 2)

print(Cylinder().volume())
print(Cylinder().surface_area())


# 6
def sphere(radius):
    """caculates the volume and surface area of a sphere. """
    volume = (4 / 3) * (math.pi * (radius ** 3))
    surface_area = 4 * math.pi * (radius ** 2)
    print("Volume of sphere: {}".format(round(volume, 3)))
    print("Surface area of sphere: {}".format(round(surface_area, 3)))
    return volume, surface_area

# sphere(2)


# 7
def length_angle(diameter, angle_degree):
    """caculates the surface area of a sector of a circle """
    sector = (360 / angle_degree)
    surface_area = (math.pi * diameter) / sector
    return round(surface_area, 2)

# print(length_angle(8, 45))


# 8
def sector(radius, angle_degree):
    """caculates the area of a sector of a circle  """
    sector = (360 / angle_degree)
    area = (math.pi * (radius ** 2)) / sector
    return round(area, 2)

# print(sector(4, 45))


# 9
def discriminant_value(x, y, z):
    # y^2 - 4xz,      x=4, y=0, z=-4 === 64
    """ return the discriminant value which is y^2 - 4xz"""
    return (y**2 - (4 * x * z))

# print(discriminant_value(4,0,-4))


# 10
def smallest_multiple_list(n):
    # 360360 
    factor = ([number for number in range(n, 1, -1) if number * 2 > n])
    print(factor)
    factors = n * 2
    while True:
        for number in factor:
            factors = factors * number
        return factors

# print(smallest_multiple_list(13)) 5434 


# 11
def sum_squared_diffrence(n=2):
    """ calculate difference between squared sum of first n
    natural numbers and sum of squared first n natural numbers.
    """
    sums = 0
    sum_squared = 0
    for num in range(1, n+1):
        sums += num
        num2 = num ** 2
        sum_squared += num2
    squared_sum = sums ** 2
    return squared_sum - sum_squared

# print(sum_squared_diffrence(12))


# 12
def power_base_sum(base, power):
    """ask someone whos good at math whats this is about. """
    return sum([int(i) for i in str(pow(base, power))])

# print(power_base_sum(4, 2))


# 13
def is_abundant_num(num):
    """checks if a number is an abundant number of the sum of all the
    divisibles of a number is greater then the number
    """
    if sum([n for n in range(1, num) if num % n == 0]) > num:
        return True
    else:
        return False

# print(is_abundant_num(12))
# print(is_abundant_num(13))


# 15
def divisors(num):
    """ returns all the divisors of a given number. """
    return [n for n in range(1, num) if num % n == 0]

print(divisors(8))
print(divisors(12))


# 14
def amicable_numbers_sum(num):
    """31624, 504, 0 """
    sum = 0
    for ints in range(1, num):
        if sum(divisors(ints)) == sum(divisors(num)):
            sum += ints
    return sum

# print(amicable_numbers_sum(9999))
# print(amicable_numbers_sum(999))
# print(amicable_numbers_sum(99))






