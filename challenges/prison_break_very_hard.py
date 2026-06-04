def freed_prisoners(block):
    if(block[0] == 0):
        return 0
    swap = False  
    index = 0
    freed_prisoners = 0
    while index < len(block):
        nobody_freed = True
        if(swap):
            while nobody_freed and index < len(block):
                if(block[index] == 0):
                    freed_prisoners += 1
                    swap = False
                    nobody_freed = False
                index += 1
        else:
            while nobody_freed and index < len(block):
                if(block[index] == 1):
                    freed_prisoners += 1
                    swap = True
                    nobody_freed = False
                index += 1
    return freed_prisoners

def main():
    print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]), "\tShould be 4")
    print(freed_prisoners([1, 1, 1]), "\tShould be 1")
    print(freed_prisoners([0,0,0]), "\tShould be 0")
    print(freed_prisoners([0,1,1,1]), "\tShould be 0")

if __name__ == '__main__':
    main()

            
        