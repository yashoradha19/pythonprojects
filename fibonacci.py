# def fib(n):

#     if n <=0:
#         print('enter a positive number')
#         return
#     a=0
#     b=1
#     if n ==1:
#         print(a)
#     else:

#         print(a)
#         print(b)
#         for i in range (2,100):
#             c=a+b
#             a=b
#             b=c
#             print(c)


# fib(5)

#printing series of numbers where last number is less than 100

def fib_lessthan100():
    a=0
    b=1
    print(a)
    print(b)
    c=a+b
    while c<100:
        print(c)
        a=b
        b=c
        c=a+b
        
fib_lessthan100()