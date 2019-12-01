__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"

#Check whether a given number is a palindrome

number= int(input("Please Enter a number to check for if it is a palindrome:"))
temp=number
rev=0

while(number>0):
    digit=number%10
    rev=rev*10+digit
    number=number//10

if(temp==rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")