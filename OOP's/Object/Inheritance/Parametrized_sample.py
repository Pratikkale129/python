class rectangle():
    def rect(self,length,breadth):
        aor = length*breadth
        print("Area of Rectangle :: ",aor)

class square(rectangle):
    def sqr(self,side):
        aos = side*side
        print("Area of Square :: ",aos)

obj1 = square()
obj1.rect(14,7)
obj1.sqr(12)