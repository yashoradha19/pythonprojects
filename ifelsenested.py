# x = 4
# r = x % 2
# if (r==0):
#     print("even")
#     if x>4:
#         print('great')
#     else:
#         print("not so great")
# else:
#     print("odd")

# x = 6
# if x==1:
#     print("one")
# elif x==2:
#     print("two")
# elif x==3:
#     print("three")
# elif x==4:
#     print("four")
# else:
#     print("wrong input")

# x = int(input("enter a number"))
# if x>0:
#     print("positive")
# elif x<0:
#     print("negative")
# else:
#     print("number is zero")


a = int(input("enter first value"))
b = int(input("enter second value"))
c = int(input("enter third number"))
if a>b and a>c:
    print("greatest number is ",a)
elif b>a and b>c:
    print("greatest number is ",b)
else:
    print("greatest number is ",c)