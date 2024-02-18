def get_factorial (num):
    factorial = 1
    for i in range (num):
        factorial = factorial * (i+1)
    return factorial

#get_factorial(5)