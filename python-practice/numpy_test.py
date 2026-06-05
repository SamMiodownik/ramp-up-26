import numpy as np

def Q1():
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    c = np.intersect1d(a, b)
    print(c)

def Q2():
    return np.arange(1, 16).reshape(3, 5).T

def Q3():
    a = Q2()
    print(a.T.flatten())

def Q4():
    a = Q2()
    a= a.T.reshape(3,5,1)
    return a

def Q5():
    a = Q4()
    a.reshape(5, 3)
    print(a)

def Q6():
    a = np.array([12, 5, 7, 15, 3, 1, 8])
    b = np.array([14, 6, 3, 11, 19, 12, 5])
    return np.setdiff1d(a, b)

def main():
    Q1()
    print(Q2())
    Q3()
    print(Q4())
    Q5()
    print(Q6())

if __name__ == "__main__":
    main()