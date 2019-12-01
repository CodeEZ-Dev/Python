__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"


def small(arr,n):
    min=arr[0]

    for i in range(1,n):
        if arr[i]<min :
            min=arr[i]
    return min

arr=[1,32,45,9,908]
n=len(arr)
result=small(arr,n)
print("The smallest in given no",result) 