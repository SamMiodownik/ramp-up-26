import math
import random

def Alpha(x):
    y = 1
    while y <= x:
        print(y)
        y += 1

def Bravo():
    total = 0
    for i in range(1, 11):
        total += i
    return total

def Charlie(x):
    return [math.cbrt(a) for a in x]

def Delta():
    while True:
        age = int(input('Please enter your age: '))
        if age < 0:
            print('Age cannot be negative. Please try again.')
        elif age > 100:
            print('Age cannot be greater than 100. Please try again.')
        else:
            return age

def Echo():
    with open('TheFile.txt', 'w') as file:
        for i in range(20):
            ran = random.randint(1, 1000)
            file.write(f'{ran}\n')

def Foxtrot(x):
    return float(x * 2)

def FavColorIfElse():
    color = input('Please enter your favorite color: ')
    if color.lower() == 'blue':
        print("Great choice.")
    elif color.lower() == 'red':
        print("Poor choice.")
    elif color.lower() == 'green':
        print("Not a bad choice.")
    else:
        print("Sorry, that's not a primary color.")

def FavColorSwitch():
    color = input('Please enter your favorite color: ')
    match color.lower():
        case 'blue':
            print("Great choice.")
        case 'red':
            print("Poor choice.")
        case 'green':
            print("Not a bad choice.")
        case _:
            print("Sorry, that's not a primary color.")

def RandomNumber():
    rand = random.randint(1, 100)
    if rand < 50:
        print("You chose a number less than 50.")
    if rand > 50:
        print("You chose a number more than 50.")

def Golf():
    return random.randint(1, 6)

def Hotel():
    counter = 1
    while True:
        if Golf() == Golf():
            return counter
        counter += 1

def India(x):
    for a in x:
        if a % 2 == 0:
            print(0)
        else:
            print(1)

def Juliet(x):
    if x % 2 == 0:
        return True
    return False

def Kilo(x):
    with open('TheFile.txt', 'r') as file:
        for a in x:
            file.write(f'{a/2}\n')

def PayCalculator():
    PAY_RATE = 50
    hours_worked = int(input('Please enter the number of hours worked: '))
    if hours_worked > 10:
        print(PAY_RATE * hours_worked)
    else:
        print(0)

def Lima(name, age):
    enteredName = input('Please enter your name: ')
    name = enteredName
    attempts = 0
    while attempts < 3:
        enteredAge = int(input('Please enter your age: '))
        if(enteredAge > -1 and enteredAge < 101):
            age = enteredAge
            break
        else:
            attempts += 1
    if attempts == 3:
        age = 0

def CelsiusFarenheit():
    for c in range(-20, 21):
        print(f"Celsius: {c}\tFahrenheit: {9/5 * c + 32}")

def Fibbonacci():
    a = 1
    b = 1
    for i in range(20):
        print(a)
        a, b = b, a + b

def Mike(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def November(g):
    if g < 70:
        print('You did not pass')
    elif g < 80:
        print('You got a C')
    elif g < 90:
        print('You got a B')
    else:
        print('You got an A')

def main():
    #print(Delta())
    #for i in range(11):
    #    print(Foxtrot(2**i))
    Alpha(10)
    print(Bravo())
    print(Charlie([1, 8, 27, 64, 125]))
    Echo()
    FavColorIfElse()
    FavColorSwitch()
    RandomNumber()
    print(Hotel())
    India([1, 2, 3, 4, 5])
    print(Juliet(4))
    print(Juliet(5))
    Kilo([1, 2, 3, 4, 5])
    PayCalculator()
    Lima('', 0)
    CelsiusFarenheit()
    Fibbonacci()
    print(Mike(29))
    print(Mike(30))
    November(65)

if __name__ == "__main__":
    main()
    
    
    