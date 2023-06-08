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