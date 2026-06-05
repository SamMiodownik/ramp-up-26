import itertools

def crack_pincode(pincode):
    dct = create_neighbors_dict()
    a = [None]*len(pincode)
    index = 0
    for index in range(len(pincode)):
        a[index] = dct[pincode[index]]
    lst = list(itertools.product(*a))
    final = []
    for tuple in lst:
        word = ""
        for number in tuple:
            word += number
        final.append(word)
    return final

def create_neighbors_dict():
    return {
        '0' : ('0','8'),
        '1' : ('1','2','4'),
        '2' : ('1','2','3','5'),
        '3' : ('2','3','6'),
        '4' : ('1','4','5','7'),
        '5' : ('2','4','5','6','8'),
        '6' : ('3','5','6','9'),
        '7' : ('4','7','8'),
        '8' : ('0','5','7','8','9'),
        '9' : ('6','8','9')
    }

def main():
    print(crack_pincode("0"))
    print(crack_pincode("2"))
    print(crack_pincode("007"))

if __name__ == '__main__':  main()

