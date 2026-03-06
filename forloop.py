#sequence starts from 11 until 20 with iteration 2
# for i in range (11,21,3):
#     print(i)
# for i in range (20,10,-1):#to print in reverse sequence
#     print(i)

# for i in range (1,21):#print numbers expect that divisible by 5
#     if i%5!=0:
#         print(i)

for i in range(1,501): # print all the perfect squares between 1,500 
    if i**0.5==int(i**0.5):#0.5 is same as square root,int will consider only whole number
        print(i)
        