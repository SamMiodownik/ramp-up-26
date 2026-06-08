def longest_substring(string):
    longest = string[0]
    index = start = 0
    while index < len(string):
        even = isEven(int(string[index]))
        index +=1
        if index == len(string) or isEven(int(string[index])) == even:
            if len(string[start:index]) > len(longest):
                longest = string[start:index]
            start = index
    return longest 

def isEven(x):
    return x % 2 == 0

def main():
    print(longest_substring("225424272163254474441338664823"), "\tShould be '272163254'")
    print(longest_substring("594127169973391692147228678476"), "\tShould be '16921472'")
    print(longest_substring("721449827599186159274227324466"), "\tShould be '7214'")
    print(longest_substring("222222222222221212121"), "\tShould be 21212121'")

if __name__ == '__main__':  main()