class sample1:
    def func1(self):
        print("This is Base class")

class sample2(sample1):
    def func1(self):
        print("This is Derived Class")

obj = sample2()
obj.func1()