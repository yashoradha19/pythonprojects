#single level ,multi level and multiple level inheritence- parent/super class->child/subclass

class A:
    def __init__(self):
        print('in A init')



    def feature1(self):
        print("feature 1 is working")
    
    def feature2(self):
        print("feature 2 is working")

class B:

    def __init__(self):
        # super().__init__()
        print("in B init")

    def feature1(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("init of c")
    def feature4(self):
        print("feature 4 is working")
    
    def feat(self):
        super().feature2()

# c1=C()
# c1.feature1()

a1 =C() #C has two super classes but A on the left han dside is called

a1.feature1() #MRO-method resolution order calls left hand side first.here both A and B have feature 1 but A is called

a1.feat()   
    