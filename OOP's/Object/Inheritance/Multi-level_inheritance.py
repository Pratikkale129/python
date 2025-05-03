# # Multi-level Inheritance
# class ver1:
#     def version_2000(self):
#         print("Nokia 1203")

# class ver2(ver1):
#     def version_2010(self):
#         print("Nokia corby 20MP")

# class ver3(ver2):
#     def version_2020(self):
#         print("Nokia lumia 2020")

# obj = ver3()
# obj.version_2020()
# obj.version_2010()
# obj.version_2000()


class person_info():
    def details(self):
        print("------------------------------")
        print("Name   :: Rakesh Sharma")
        print("Email  :: rcsharma@gmail.com")
        print("Gender :: Male")
        print("DOB    :: 19/08/2004")
        print("------------------------------")
        print("\n")

class Registration(person_info):
    def record(self):
        print("------------------------------")
        print("Mobile     :: 7767820048")
        print("Password   :: Pratik@124578")
        print("C_password :: Pratik@124578")
        print("------------------------------")
        print("\n")

class Sign_in(person_info):
    def log_in(self):
        print("------------------------------")
        print("Email ID :: rcsharma@gmail.com")
        print("Password :: Pratik@124578")
        print("------------------------------")

obj = Sign_in()
obj.details()
obj.log_in()

obj1 = Registration()
obj1.details()
obj1.record()