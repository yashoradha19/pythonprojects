# nums = [12,19,26,18]

# for num in nums:
#     if num % 5==0:
#         print(num)
#         break
# else:
#     print("not found")

num = 6
for i in range (2,num):
    if num % i==0:
        print("not prime")
        break
else:
    print("prime")


