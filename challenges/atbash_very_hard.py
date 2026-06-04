def atbash(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    bachwards_uppercase = uppercase[::-1]
    backwards = alphabet[::-1]
    new_word = ""
    for char in word:
        if char in alphabet:
            new_word += backwards[alphabet.index(char)]
        elif char in uppercase:
                new_word += bachwards_uppercase[uppercase.index(char)]

        else:
            new_word += char
    return new_word

def main():
    print(atbash("apple"), "\tShould be zkkov")
    print(atbash("Hello World!"), "\tShould be Svool Dliow!")

if __name__ == "__main__":    main()