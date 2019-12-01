__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"

sum=0
number=int(input("Enter a no to be checked as  a STRONG no : "))
temp=number

while(number):
    i=1
    f=1
    r=number%10
    while(i<=r):
        f=f*i
        i=i+1
        sum=sum+f
        number=number//10
       # print(sum)
if(sum==temp):
    print("WOW...The number is a strong no")
else:
    print("Sorry...!The Number is not a strong number")