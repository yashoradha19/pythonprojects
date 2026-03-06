#a function that does not have name is called anonymous function and they are defined using lambda functions or lambda expressions

# f=lambda a,b:a+b #lambda
# result=f(5,6)
# print(result)


#using filter()to filter out even numbers from the list
# def is_even(n):
#     return n%2==0
# nums=[1,2,3,4,5,6,7,8,9]
# evens=list(filter(is_even,nums))
# print(evens)

#doing the same listing of even numbers but by using lambda

# nums=[1,2,3,4,5,6,7,8,9]
# evens=list(filter(lambda n:n%2==0,nums))
# print(evens)


#using of map(),reduce()and lambda()
from functools import reduce
nums=[1,2,3,4,5]

evens=list(filter(lambda n:n%2==0,nums))
print(evens)
doubles=list(map(lambda n:n*2,evens))
print(doubles)

sum=reduce (lambda a,b:a+b,doubles)
print(sum)
