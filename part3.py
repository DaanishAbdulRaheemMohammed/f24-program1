# Name: [Daanish Mohammed]
# Date: [4/9/20204]
# Assignment: Factorial Digit Sum Largest Palindrome Product

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def product_num_palindrome(num1, num2):
    max_value = 0
    
    for i in range(10**(num1-1), 10**num1):
        for j in range(10**(num2-1), 10**num2):
            product = i * j
            if is_palindrome(product) and product > max_value:
                max_value = product
    
    # DO NOT REMOVE
    print(f'Max number for {num1} by {num2} is {max_value}')

if __name__ == '__main__':
    product_num_palindrome(2, 2)  # test case
    product_num_palindrome(3, 3)