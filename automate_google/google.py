# for x in range(5):
#     print(x)

# for i in range(50):
#     print(i)


# nested loop to print every dominoe with no doubles

for left in range(7):
    for right in range(left, 7):
        print(f'[{left} | {right}]', end=' ')
    print()