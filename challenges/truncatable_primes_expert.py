def truncatable_left(x):
    if not prime(x):
        return False
    word = str(x)
    if len(word) == 1:
        return True
    return truncatable_left(int(word[1:]))

def truncatable_right(x):
    if not prime(x):
        return False
    word = str(x)
    if len(word) == 1:
        return True
    return truncatable_right(x % 10)

def truncatable(x):
    word = str(x)
    for char in word:
        if char == "0":
            return False
    left = truncatable_left(x)
    right = truncatable_right(x)
    if left and right:
        return "both"
    elif left:
        return "left"
    elif right:
        return "right"
    else:
        return False

def prime(x):
    if x == 1:
        return False
    number = 2
    while number < x:
        if x % number == 0:
            return False
        number += 1
    return True

def main():
    print(truncatable(9137), "\tShould be 'left'")
    print(truncatable(5939), "\tShould be 'right'")
    print(truncatable(317), "\tShould be 'both'")
    print(truncatable(5), "\tShould be 'both'")
    print(truncatable(139), "\tShould be False")
    print(truncatable(103), "\tShould be False")

if __name__ == '__main__':  main()




