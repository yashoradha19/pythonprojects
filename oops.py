#object is an instance of a class:consider class as a design/blue print in which it has 
#attributes- variables and behaviour-methods(function)

# class computer:
#     def config(self):
#         print('i5,16gb,iTB')

# com1=computer()
# com2=computer()


# we can call object by using class like this
# computer.config(com1)
# computer.config(com2)

# com1.config()
# com2.config()


# now we get see how to use variable.here each object will have its own data/variable and method  they work together

# class computer:

#     def __init__(self,cpu,ram): #init is called as constructor
#         self.cpu=cpu
#         self.ram=ram



#     def config(self):
#         print("config is",self.cpu)

# com1=computer('i5',16)
# com2=computer('Ryzen 3',8)

# com1.config()
# com2.config()


class computer:
    def __init__(self):
        self.name="radha"
        self.age=24
    
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1=computer()
c1.age=25
c2=computer()

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")

print(c1.name)
print(c2.name)
