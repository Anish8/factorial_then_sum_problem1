Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # This Python Program finds the factorial of a number

def factorial(num):
    """This is a recursive function that calls
   itself to find the factorial of given number"""
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


# We will find the factorial of this number
num = int(input("Enter a Number: "))

# if input number is negative then return an error message
# elif the input number is 0 then display 1 as output
# else calculate the factorial by calling the user defined function


if num < 0:
    print("Factorial cannot be found for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
   def sum_digits(n):
        s = 0
    while n:
        s += n % 10
        n //= 10
    return s
    
print("\n Sum of the digits of Given Number = %d" %Sum)
