def adjacent(list, node1, node2):
    return bool(list[node1][node2])

def main():
    list = [ [ 0, 1, 0, 0 ], [ 1, 0, 1, 1 ], [ 0, 1, 0, 1 ], [ 0, 1, 1, 0 ]]
    print(adjacent(list, 0, 1),"\tShould be True")
    print(adjacent(list, 0, 2),"\tShould be False")

    list = [ [ 0, 1, 0, 1, 1 ], [ 1, 0, 1, 0, 0 ], [ 0, 1, 0, 1, 0 ], [ 1, 0, 1, 0, 1 ], [ 1, 0, 0, 1, 0 ] ]
    print(adjacent(list, 0, 3),"\tShould be True")
    print(adjacent(list, 1, 4),"\tShould be False")


if __name__ == "__main__":
    main()