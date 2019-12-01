__author__ = "Muralidharan V"
__copyright__ = "Copyright 2019, The CodeEZ-IoT"

R=int(input("Enter the No of rows of the matrix please.."))
C=int(input("Enter the No of columns of the matrix please..."))

matrix =[]
print("Enter the entries rowise: ")

for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j],end=' ')
    print()