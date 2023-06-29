# for x in range(5):
#     print(x)

# for i in range(50):
#     print(i)


# nested loop to print every dominoe with no doubles

# for left in range(7):
#     for right in range(left, 7):
#         print(f'[{left} | {right}]', end=' ')
#     print()

# def multiplication_table(start, stop):
#     for x in range(start, stop + 1):
#         for y in range(start, stop + 1):
#             print(str(x*y), end=" ")
#         print()

# multiplication_table(1, 3)
# multiplication_table(10, 30)



# teams = ['pandas', 'dragons', 'rats', 'snakes', 'clippers', 'sharks']

# for home_team in teams:
#     for away_team in teams:
#         if home_team != away_team:
#             print(f"Home: {home_team.capitalize()} vs Away: {away_team.capitalize()}")

# def factorial(n):
#     if n < 2:
#         return 1
#     return n * factorial(n - 1)
    
# print(factorial(10))


# def recursive_function(parameters):
#     if base_case_condition(parameters):
#         return base_case_value
#     recursive_function(modified_parameters)


# def count_users(group):
#   count = 0
#   for member in count_members(group):
#     count += 1
#     if is_group(member):
#       count += count_users(member)
#   return count





num1 = 0
num2 = 2

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3
    print(num1 + num2)
    