class cars:
    def manual(self,gear,brand):
        print("---------- || Manual Cars || ----------")
        print("Gears    :: ",gear)
        print("Car Brand:: ",brand)

class car:
    def Suv(self,Hachback,engine,):
        print("---------- || SUV Cars || ----------")
        cc = 1200
        tor = 60
        
        milaege = (cc*tor)/600
        milaege = milaege/3.4
        print("Milaege :: ",milaege)

        print("Company name :: ",Hachback)
        print("Engine type  :: ",engine)


class Electric(cars,car):
    def automatic(self,modes,battery):
        print("---------- || Automatic Cars || ----------")
        print("Car Mode    :: ",modes)
        print("Battery Life:: ",battery)

obj1 = Electric()
obj1.manual(6,"Dodge")
obj1.automatic("Autopilot",1000)
obj1.Suv("Lamborghini urus",12)