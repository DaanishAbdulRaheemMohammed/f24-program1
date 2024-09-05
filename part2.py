# Name: [Daanish Mohammed]
# Date: [4/9/20204]
# Assignment: The 1000-Digit Fibonacci Number

def digitis_in_fibo(digits):
    a, b = 1, 1
    index = 2  # Starting from F2
    
    while len(str(b)) < digits:
        a, b = b, a + b
        index += 1
    
    # DO NOT ERASE
    print(f'For index {index}, it contains {len(str(b))} digits')

if __name__ == '__main__':
    digitis_in_fibo(3)  # test case
    digitis_in_fibo(1000)
