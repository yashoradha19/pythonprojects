# def fact(x):
#     f=1
#     for i in range(1,x+1):
#         f=f*i
#     return f
    
# x=int(input('enter a value: '))
# result=fact(x)
# print(result)

#recurssion in python-a function calling itself-inorder to find out limit sys.getrecurssionlimit

# import sys
# sys.setrecursionlimit(2000)# inorder to repeat 2000 times we have to change the default limit
# print(sys.getrecursionlimit())
# i=0
# def greet():
#     global i
#     i+=1
#     print('hello',i)
#     greet()
# greet()

#factorial of number using recursion
def fact(n):
    if (n==0):
        return 1
    return n*fact(n-1)
    

result=fact(5)
print(result)