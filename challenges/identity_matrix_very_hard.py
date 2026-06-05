import numpy as np
def id_mtrx(x):
    if not isinstance(x, int):
        return "Error"
    if x > 0:
        return id_mtrx_pos(x) 
    return id_mtrx_neg(abs(x))

def id_mtrx_pos(x):
    a = np.arange(x*x).reshape(x,x)
    row = column = 0
    while row < x:
        while column < x:
            if(row == column):
                a[row][column] = 1
            else:
                a[row][column] = 0
            column +=1
        row +=1
        column = 0
    return a

def id_mtrx_neg(x):
    a = np.arange(x*x).reshape(x,x)
    row = column = 0
    while row < x:
        while column < x:
            if(row + column + 1 == x):
                a[row][column] = 1
            else:
                a[row][column] = 0
            column +=1
        row +=1
        column = 0
    return a

def main():
    print(id_mtrx(3))
    print(id_mtrx(8))
    print(id_mtrx(-5))
    print(id_mtrx("4"))
    print(id_mtrx(-10))

if __name__ == '__main__':  main()