import math
import unittest

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



# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...

# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)


def row_sum_odd_numbers(n):
    return n ** 3


def filter_list(l):
    return [x for x in l if isinstance(x, int)]


def divisors(n):
    count = []
    for i in range (1, int(n ** .5) + 1):
        if n % i == 0:
            count.append(i)
            if i * i != n:
                count.append(n // i)
    return len(count)

# print(divisors(30))
# print(divisors(600))
# print(divisors(4))


def is_anagram(test, original):
    str1 = test.lower()
    str2 = original.lower()
    return sorted(str1) == sorted(str2)

# def anablam(t, o):
#     return sorted(t.lower()) == 



def fibonnaci(n):
    if n == 0 or n == 1:
        return n
    else: return (fibonnaci(n-1) + fibonnaci(n-2))

print(fibonnaci(40))


class Solution(object):
    def two_sum(self, nums, target):
        compliment_map = {}
        for i, num in enumerate(nums):
            if num in compliment_map:
                return [compliment_map[num], i]
            compliment = target - num
            compliment_map[compliment] = i
        return []
    

def disemvowel(str):
    vowels = 'aeiouAEIOU'
    result = ''

    for char in str:
        if char not in vowels:
            result += char
    
    return result

def capitals(word):
    indecies = []
    for index, char in enumerate(word):
        if char.isupper():
            indecies.append(index)
    return indecies

# Test the function
input_word = "CodEWaRs"
output_indices = capitals(input_word)
print(output_indices)  # Output: [0, 3, 4, 6]


def reverse_list(l):
    return l[::-1]


# Messi goals function

# Messi is a soccer player with goals in three leagues:

#     LaLiga
#     Copa del Rey
#     Champions

# Complete the function to return his total number of goals in all three leagues.

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga+copaDelRey+championsLeague

def messiGoals(*a):
    return sum(a)


#LIST COMPREHENSIONS
#new_list = [expression for item in iterable if condition]

#Squares of numbers from 0 - 9

#for loop
squares = []
for num in range(10):
    squares.append(num ** 2)

#list comprehension
squares = [num ** 2 for num in range(10)]

# Let's learn about list comprehensions! You are given three integers and representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by on a 3D grid where the sum of is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise. 

x = int(input())
y = int(input())
z = int(input())
n = int(input())
# list comprehension format
coordinates = [[i, j, k] for i in range(x + 1) for j in range (y + 1) for k in range(z + 1) if i + j + k != n]


x = int(input())
y = int(input())
z = int(input())
n = int(input())
#for loop format
cubic_coordinates = []
for i in range (x + 1):
    for j in range (y + 1):
        for k in range (z + 1):
            if i + j + k != n:
                cubic_coordinates.append([i, j, k])


# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given

# scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains
# . The second line contains an array of integers each separated by a space. 

n = int(input())
arr = map(int, input().split())

scores = list(set(arr))

scores.sort(reverse = True)

runner_up_score = scores[1]

print(runner_up_score)

# Write a function which takes a number and returns the corresponding ASCII char for that value.

def get_ascii_char(number):
    if 0 <= number <= 256:
        return chr(number)
    else:
        return "Invalid input. Please provide a number between 0 and 127."
    
def get_char(num):
    return chr(num)

class TestGetAsciiChar(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(get_ascii_char(65), "A")
        self.assertEqual(get_ascii_char(97), "a")
        self.assertEqual(get_ascii_char(33), "!")
        self.assertEqual(get_ascii_char(126), "~")

    def test_invalid_input(self):
        self.assertEqual(get_ascii_char(-1), "Invalid input. Please provide a number between 0 and 127.")
        self.assertEqual(get_ascii_char(128), "Invalid input. Please provide a number between 0 and 127.")
        self.assertEqual(get_ascii_char(2000), "Invalid input. Please provide a number between 0 and 127.")

if __name__ == '__main__':
    unittest.main()