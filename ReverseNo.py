__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"

number=int(input("Enter Number : "))
rev=0

while(number>0):
    digit=number%10
    rev=rev*10+digit
    number=number//10

print("Reverse of the number is now : ",rev)
