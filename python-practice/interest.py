interest_rate = int(input('Please enter the interest rate\t'))
principal = int(input('Please enter the principal amount\t'))
years = int(input('Please enter the number of years\t'))

final_amount = principal * (1 + interest_rate)**years
print(f'the final amount is {final_amount:.2f}')