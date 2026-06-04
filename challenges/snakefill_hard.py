def snakefill(x):
    max = x**2
    size = 1
    counter = 0
    while True:
        size *= 2
        if size >= max:
            return counter
        else:
            counter += 1

def main():
    print(snakefill(3), "\tShould be 3")
    print(snakefill(6), "\tShould be 5")
    print(snakefill(24), "\tShould be 9")

if __name__ == "__main__":    main()
    