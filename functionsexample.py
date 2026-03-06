# def add_sub(x,y):
#     c=x+y
#     d=x-y
#     return c,d

# result1,result2=add_sub(5,4)
# print(result1,result2)

# def update(x):
#     print(id(x))
#     x=8
#     print(id(x))

#     print(x)
# a=10
# print(id(a))
# update(a)
# print(a)

# def person(name,age):#formal arguments
#     print(name)
#     print(age)
# person('radha',24)#actual arguments-positionarguments
# person(age=24,name='radha')#keyword arguments

#for default arguments at def person(name,age=18)give the default value .in that case it can be given as perosn('radha')not need to give the default value

#variable length arguments
# def sum(a,*b):# since b is taken as tuple we have to create a for loop inorder to add all the values 
#     c=a
#     for i in b:
#         c=c+i
#     print(c)
# sum(5,6,34,78)

#if we have to pass multiple date with thehelp of keyword then instead of *d we have to use **d

# local and global variable
# a=10
# def something():
#     #global a
#     a=15
#     print('in fun',a)
# something()
# print('outside',a)

#how to change global variable without effecting the local variable is by using globals()
# a=10
# print(id(a))
# def something():
#     a=9
#     x=globals()['a']
#     print(id(x))

#     print('in fun',a)
#     globals()['a']=15
# something()
# print('outside',a)


def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=list(map(int,input('enter a list of values: ' ).split()))
even,odd=count(lst)

print(even)
print(odd)