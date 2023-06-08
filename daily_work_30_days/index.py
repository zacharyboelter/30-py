import math

def euclid_dist(x1, x2, y1, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1) ** 2)
    return distance

print(euclid_dist(2, 3, 10, 8))