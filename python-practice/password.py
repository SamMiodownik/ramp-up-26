while True:
    pwd = input('Please enter your password: ')

    length = False
    number = False
    upper = False
    lower = False
    special_char = False

    if len(pwd) >= 8:
        length = True

    for char in pwd:
        if char.isdigit():
            number = True
        elif char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif not char.isalnum():
            special_char = True
    if length and number and upper and lower and special_char:
        print('Password is valid')
        break
    else:
        print('Password is not valid.')
        if not length:
            print('Password must be at least 8 characters long.')
        if not number:
            print('Password must contain at least one number.')
        if not upper:
            print('Password must contain at least one uppercase letter.')
        if not lower:
            print('Password must contain at least one lowercase letter.')
        if not special_char:
            print('Password must contain at least one special character.')