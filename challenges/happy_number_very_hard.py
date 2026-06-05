def is_happy(x):
    if x == 1:
        return True
    if x == 4:
        return False
    newx = 0
    strx = str(x)
    for char in strx:
        newx += int(char)**2
    return is_happy(newx)

def main():
    print(is_happy(67), "\tShould be False")
    print(is_happy(89), "\tShould be False")
    print(is_happy(139), "\tShould be True")
    print(is_happy(1327), "\tShould be False")
    print(is_happy(2871), "\tShould be False")
    print(is_happy(3970), "\tShould be True")

if __name__ == '__main__':  main()