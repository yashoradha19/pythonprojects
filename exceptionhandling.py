a=5
b=2

try:
    print("resource open")
    print(a/b)
    k=int(input("enter  a number"))
    print(k)

except ZeroDivisionError as e:
    print("you cannot divide a number by zero",e)

except ValueError as e:
    print('invalid input')

except Exception as e:
    print('something went wrong')


finally:
    print('resource closed')