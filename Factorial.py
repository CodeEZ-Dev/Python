__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"

def factorial(n):
    '''This is a factorial return function'''
    return 1 if(n==1 or n==0) else n* factorial(n-1)

num=int(input("Enter a factorial no:"))

print("factorial of",num,"is", factorial(num))