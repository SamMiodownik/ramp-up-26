print(3, end = ' ')
for i in range(4, 1001):
    for char in str(i):
        if char == '3':
            print('|', i, end = ' ')
print()