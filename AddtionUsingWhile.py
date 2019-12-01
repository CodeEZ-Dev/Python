__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"

number=int(input("Enter Number : "))
total=0

while(number>0):
    digit=number%10
    total=total+digit
    number=number//10

print("The Total sum of digit is", total)