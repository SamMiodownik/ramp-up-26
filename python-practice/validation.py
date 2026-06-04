counter = 0

while counter < 3:

    name = input("Please enter your name\t")
    age = input("Please enter your age\t")

    if name.isalpha() and age.isdigit() and int(age) > 0 and int(age) < 100:
        print('Acceptable')
        break
    else:
        if counter < 2:
            print("Invalid input. Please try again.")
        else:
            print('Unacceptable')
        counter += 1
