def can_see_stage(stadium):
    see = True
    x , y = len(stadium) - 1, 0
    while y < len(stadium[0]):
        if x == 0:
            y += 1
            x = len(stadium) - 1
        else:
            if stadium[x][y] <= stadium[x-1][y]:
                see = False
                break
            x -= 1
    return see

def main():
    print(can_see_stage([[1, 2, 3],[4, 5, 6],[7, 8, 9]]), "\tshould be True")
    print(can_see_stage([[0, 0, 0],[1, 1, 1],[2, 2, 2]]), "\tshould be True")
    print(can_see_stage([[2, 0, 0],[1, 1, 1],[2, 2, 2]]), "\tshould be False")
    print(can_see_stage([[1, 0, 0],[1, 1, 1],[2, 2, 2]]), "\tshould be False")

if __name__ == '__main__':
    main()



