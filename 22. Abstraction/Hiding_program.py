class test1:
    __x = 12
    y = 4
    def func_1(self):
        print("This is 1st Function")

class test2(test1):
    def func_2(self):
        print("This is 2nd Function")
        print(self.x)

obj = test2()
obj.func_2()