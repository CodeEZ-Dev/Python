__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"

def largest(arr,n):
    max=arr[0]

    for i in range(1,n):
        if arr[i] > max:
            max=arr[i]
    return max

arr =[1,32,45,9,908]
n=len(arr)
result=largest(arr,n)
print("Largest in given array is ", result)