def lcm(list):
    number = max(list)
    while True:
        divisible = True
        for num in list:
            if number % num != 0:
                divisible = False
        if divisible:
            return number
        else:
            number += 1

def main():
    print(lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]), "\tShould be 2520")
    print(lcm([5]), "\tShould be 5")
    print(lcm([5, 7, 11]), "\tShould be 385")
    print(lcm([5, 7, 11, 35, 55, 77]), "\tShould be 385")

if __name__ == "__main__":  main()
