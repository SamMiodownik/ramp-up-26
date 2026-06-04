def stutter(word):
    return word[0:2] + "..." + word[0:2] + "..." + word + "?"

def main():
    print(stutter("incredible"))
    print(stutter("enthusiastic"))
    print(stutter("outstanding"))

if __name__ == "__main__":    main()