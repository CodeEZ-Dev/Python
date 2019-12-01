__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"

'''calculate the avg of no in a given list'''

list_Of_No=int(input("Enter the number of elements to be entered : "))
list_of_element=[]

for i in range(0,list_Of_No):
    element=int(input("Enter element : "))
    list_of_element.append(element)
    
avg=sum(list_of_element)/list_Of_No
print("Average of elements in the list",round(avg,2))