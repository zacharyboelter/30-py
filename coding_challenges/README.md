# Code Challenges w/ explanations.

### 1. Find an Euclidian distance between (2, 3) and (10, 8). (codewars)
Function takes four parameters, one for each x and y point (2 dimentions). Take the square root of (x2 - x1) ^ 2 and add it to y axies. 

### 2. Given an integral number, determine if it's a square number. (codewars)
Check if n is less than zero to remove negative intergers. 
Get square root of n, check if n equals square ** 2.

### 3. Summation. (codewars)
Set sum to zero. For loop that starts at 1 and goes to num (parameter) + 1. Add each iteration to sum. Return.

### 4. Regex Validate PIN Code. (codewars)
Check if PIN is length of either 4 or 6. Check if PIN is digits. Return if true.

### 5. Return sum of odd nums. (codewars)
Return n^3.

### 6. List Filtering
Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

### 7. Count the number of divisors
Set count to empty list. Iterate over the numbers from 1 to the square root of n. Check if n is divisible by current number. If n is divisible by the current number, then that number is added to the list of divisors. Check if the current number is the sqrt of n. If the current number is not the square root of n, then n is divided by the current number and the result is added to the list of divisors. return the length of count.

### 8. Anagram Detection
Set parameters to variables, lower case. If, when sorted, they match, return true. Else, false.

### 9. Two Sum Problem 

The **Two Sum** problem involves finding two numbers in an array that add up to a given target. We are required to return the indices of these two numbers.

To solve this problem, we can use a hashmap (dictionary in Python) to store the complement of each number we encounter. Here's how the solution works:

1. We start by creating an empty hashmap called `complement_map`. This hashmap will store the complements of the numbers we encounter.

2. We iterate through the input array `nums` using a loop. For each number `num` at index `i`, we perform the following steps:

3. Check if the current number `num` is already in the `complement_map` hashmap. If it is, that means we have found a pair of numbers whose sum is equal to the target. We can retrieve the index of the complement from the hashmap and return it along with the current index `i` as the answer.

4. If the current number is not in the hashmap, it means we haven't found its complement yet. So, we calculate the complement by subtracting the current number from the target. This gives us the value that, when added to the current number, will give us the target sum.

5. We add the complement to the `complement_map` hashmap, using the complement value as the key and the current index `i` as the value. By doing this, we are storing the complement for future reference.

6. If we have iterated through the entire array and haven't found a solution yet, we return an empty list `[]` to indicate that no solution exists.

By using this approach, we can find the indices of two numbers in the input array that add up to the target sum.

The time complexity of this solution is O(n) since we iterate through the input array once. The space complexity is O(n) to store the complement hashmap.
