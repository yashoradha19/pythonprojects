# pos=-1
# def search(list,n):
#     i = 0
#     while i <len(list):
#         if list[i]==n:
#             globals()['pos']=i
#             return True
#         i=i+1
#     return False



# list=[1,2,3,4,5]
# n=3

# if search(list,n):
#     print("found at",pos+1)
# else:
#     print("not found")

#linear search using for loop

pos=-1

def search (list,n):
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return i
        



list=[1,2,3,4,5]
n=int(input("enter a value"))

if search(list,n):
    print("found at ", pos)
else:
    print("not found")