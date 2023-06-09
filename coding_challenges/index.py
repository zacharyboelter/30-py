import math

# Euclidean Distance
# Find an Euclidian distance between (2, 3) and (10, 8)

def euclid_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1) **2 )
    return distance


# def is_square(n):
#     if n < 0:
#         return False
    
#     square = math.isqrt(n)
#     return square ** 2 == n


def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0



# def summation(num):
#     sum = 0
#     for i in range(1, num + 1):
#         sum += i
#     return sum



def summation(num):
    return sum(range(num + 1))

# def validate_pin(pin):
#     if len(pin) == 4 or len(pin) == 6:
#         if pin.isdigit():
#             return True
#     return False

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin('3333'))
print(validate_pin('444444'))
print(validate_pin('123d'))
print(validate_pin('123'))
print(validate_pin('....'))