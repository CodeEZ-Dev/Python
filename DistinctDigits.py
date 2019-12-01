__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"

num1=int(input("Enter first DIGIT of the Num : "))
num2=int(input("Enter secound DIGIT of the Num : "))
num3=int(input("Enter third DIGIT of the Num : "))

l=[]
l.append(num1)
l.append(num2)
l.append(num3)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(l[i],l[j],l[k])