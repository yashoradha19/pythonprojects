#types of variables


# class car: # varibales defined outside are class varibales

#     wheels=4
#     def __init__(self):
#         self.mil=10 #  variables inside inint are instance variables.these are called instance variables when change of one variable will not effect other variables
#         self.com="bmw"

# c1=car()
# c2=car()
# c1.mil=8

# car.wheels=5

# print(c1.mil,c1.com,c1.wheels)
# print(c2.mil,c2.com,c2.wheels)


# #types of methods. -instance methods,class methods,static methods


# class student:


#     school = "usf"

#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
    
#     def avg(self):   #instance method
#         return(self.m1+self.m2+self.m3)/3
    
#     @classmethod  #class method
#     def getschool(cls):
#         return cls.school
    
#     @staticmethod
#     def info():#static method
#         print("this is student class this has nothing to do with student or class")
    




# s1 = student(23,24,26)
# s2 = student(34,35,36)

# print(s1.m1)
# print(s1.avg())
# print(student.getschool())

#class inside a class example


class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student('radha',1)
s2=student('navin',3)

print(s1.name,s1.rollno)


s2.show()

# lap1=student.laptop()