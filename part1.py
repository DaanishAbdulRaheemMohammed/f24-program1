# Name: [Daanish Mohammed]
# Date: [4/9/20204]
# Assignment: Factorial Digit Sum

import math

def number_of_digits(number):
    # Calculate the factorial of the number
    factorial = math.factorial(number)
    
    # Convert the factorial result to a string and sum its digits
    number_sum = sum(int(digit) for digit in str(factorial))
    
    # DO NOT erase
    print(f'The sum of digits for {number}! is: {number_sum}')

if __name__ == '__main__':
    number = 100
    number_of_digits(number)