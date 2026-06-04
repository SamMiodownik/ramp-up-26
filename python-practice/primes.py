print(101, end = ' ')
for i in range(103, 1000, 2):
    prime = True
    for j in range(3, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(f"| {i}", end = ' ')