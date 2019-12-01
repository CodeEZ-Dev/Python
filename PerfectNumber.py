__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"


num=int(input("Enter any no : "))
sum=0
for i in range(1,num):
    if(num % i ==0):
        sum=sum+i
if(sum == num):
    print("The number is a perfect no!")
else:
    print("The number is not a perfect no!")
