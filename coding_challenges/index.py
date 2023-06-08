import math

# Euclidean Distance
# Find an Euclidian distance between (2, 3) and (10, 8)

def euclid_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1) **2 )
    return distance

print(euclid_distance(2, 4, 6, 8))
print(euclid_distance(2, 3, 10, 8))
print(euclid_distance(10, 4, 6, 8))
print(euclid_distance(2, 60, 6, 8))


def is_square(n):
    if n < 0:
        return False
    
    square = math.isqrt(n)
    return square ** 2 == n
print(is_square(0))
print(is_square(-1))
print(is_square(25))
print(is_square(26))
print(is_square(100))
print(is_square(121))