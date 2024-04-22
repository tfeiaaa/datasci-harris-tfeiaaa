# Your names and CNET IDs here

"""
INSTRUCTIONS

All members of your team should attempt all excercises

When the time comes to commit only _one_ of you should commit
"""

"""
EXCERCISE 1

Create a function named calculate_average that that takes a list of numbers as 
an argument and returns the average. Ensure that the function returns 
an empty list by returning 0.

Hint: len(list) will return the length of a list
"""

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)

print(calculate_average([0,1,2]))
"""
def calculate_average(numbers):
    # Check if the list is empty and return 0 if it is
    if not numbers:
        return 0

    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  


print(calculate_average([0, 1, 2]))  
print(calculate_average([]))  
1.0
0

EXCERCISE 2

Create a function named is_prime that takes an integer as an input and returns
True (a boolean) if the number is a prime number and False if it is not. 
A prime number is a number that is only divisible by 1 and itself. Remember 
to include the following error messages:

    1. If the number is a float instead of an integer, return "Error 001"
    2. If the number is a string instead of an integer, return "Error 002"

Hint: x is divisible by y if and only if x % y = 0

Hint: You will, at some point, have to loop over all integers from 0 to x

Hint: the command isinstance(x, int) will return True if x is an instance of 
the int data type. The same is true for float and str data types
"""

def is_prime(num):
    if isinstance(num, float):
        return "Error 001"
    
    if isinstance(num, str):
        return "Error 002"
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

"""

def is_prime(num):
    if isinstance(num, float):
        return "Error 001"
    
    if isinstance(num, str):
        return "Error 002"
    
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True



EXCERCISE 3

Create a function named valid_password that takes a string as an input. It will
return True if (1) the string is longer than 8 characters and (2) has at least
one upper case character and (3) has at least one lower case character and
(4) has one digit. Otherwise, it will return False.

Hint: A string is a container that contains characters. You can loop over 
these characters by using a for loop. Each character you loop over is a string

Hint: The line of code "return False" will end the function and can be used in
different lines - you don't have to reserve it for the very end!

Hint: The following methods belong to string objects and return True if the
string they are attached to contains only upper case letters, lower case letters,
and digits respectively: 
    .isupper()
    .islower()
    .isdigit()
"""

def valid_password(password):
    if len(password) <= 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return True
    else:
        return False
        
print(valid_password("QWERTYuiop123"))

def valid_password(password):
    if len(password) <= 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit
        
valid_password("QWERTYuiop123")

 True