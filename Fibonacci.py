__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"


nterms=10
number1=0
number2=1
count=0
print("THe series is as follow")

if nterms <=0:
    print("please enter a postive interger")

elif nterms ==1:
    print("Fibonacci sequence upto",nterms,":")
    print(number1)
else:
    print("Fibonacci sequence upto",nterms,":")
    while count <nterms:
        print(number1,end=' ,')
        nth=number1+number2
        number1=number2
        number2=nth
        count+=1

