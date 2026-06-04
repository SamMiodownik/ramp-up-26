def number_length(num):
    if num == 0:
        return 1
    else:
        num //= 10
        if(num == 0):
            return 1
        else:
            return 1 + number_length(num)
    
def main():
    print(number_length(0), "\tShould be 1")
    print(number_length(12345), "\tShould be 5")
    print(number_length(999999999), "\tShould be 9")

if __name__ == "__main__":
    main()