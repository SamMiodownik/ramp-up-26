def dis(price, percent):
    return price - (price * percent / 100)

def main():
    print(dis(1500, 50))
    print(dis(89, 20))
    print(dis(100, 75))

if __name__ == "__main__":    main()