class cars:
    def manual(self,gear,brand):
        print("---------- || Manual Cars || ----------")
        print("Gears    :: ",gear)
        print("Car Brand:: ",brand)

class Electric(cars):
    def automatic(self,modes,battery):
        print("---------- || Automatic Cars || ----------")
        print("Car Mode    :: ",modes)
        print("Battery Life:: ",battery)

obj1 = Electric()
obj1.manual(6,"Dodge")
obj1.automatic("Autopilot",1000)