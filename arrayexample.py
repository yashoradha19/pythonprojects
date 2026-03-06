# from array import *

# vals = array('i',[5,9,8,4,2])


# for i in range (5):
# print(vals)
# newArr=array(vals.typecode,[a*a for a in vals])
 # for e in newArr:
#     print(e)
# or
# i=0
# while i<len(newArr):
#     print(newArr[i])
#     i=i+1

# arr = array('i',[])
# n = int(input("Enter the length of the array"))

# for i in range(n):
#     x=int(input("Enter the value"))
#     arr.append(x)
# print(arr)
# val = int(input("Enter the value for search"))
# # k=0
# for e in arr:
#     if e==val:
#         print(k)
#         break
#     k=k+1
# print(arr.index(val))


#by using numpy

# from numpy import *
# arr =array([1,2,3.1,4,5])
# print(arr.dtype)
# print(arr)

#ways to create an array- array(),linspace(),logspace(),arrange(),zeros(),ones()

# arr = linspace(1,10,5)
# arr = logspace(1,40,5)
# arr = arange(1,10,2)
# arr = ones(5)
# arr = zeros(5)
# print(arr)

# arr1=array([1,2,3,4,5])
# arr2=arr1 #simple copy but here there will only be one array
# print(concatenate ([arr1,arr2]))

# arr2=arr1.view() #by using view it creates two different ids also called as shallow copy
# arr2=arr1.copy()#deep copy
# arr1[1]=7
# print(arr1)
# print(arr2)


#2D array and operations like size,reshape,flatten
from numpy import*
# arr1=array([[1,2,3,6,2,9],[4,5,6,7,5,3]])

# # print(arr1.shape)
# arr2=arr1.flatten()
# arr3=arr2.reshape(2,2,3)
# print(arr3)

# arr1=array([[1,2,3,6],[4,5,6,7]])
m = matrix('1 2 3; 6 4 5; 1 6 7')
print(m.min())
print(diagonal(m))

#multiplication of matrices
m1=matrix('1 2 3;6 4 7;1 6 5')
m2=matrix('1 2 3;6 8 5;2 6 7')
m3=m1*m2;
print(m3)