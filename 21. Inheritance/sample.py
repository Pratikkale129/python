# create base class 
class rectangle:
    def rect(self):
        l = 15
        b = 4
        aor = l * b
        print(aor)

class circle(rectangle):
    def circle(self):
        pi = 3.14
        r = 3
        aoc = pi * r * r
        print(aoc)

obj1 = circle()
obj1.circle()
obj1.rect()