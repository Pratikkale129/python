# # def arg_function(name):
# #     print('Hello',name)

# # arg_function('Jarvis')
# # arg_function('Alexa')
# # arg_function('Google Assistant')
# def args(fname,lname):
#     print("My name is",fname,lname)

# args('Prathamesh','Khodke')

def args(fname,lname):
     
    un = input(str("Enter the User name ::"))
    ps = input(int("Enter the Password  ::"))
    if un==fname:
        print("Username Accepted...")
    elif ps==lname:
        print("Password Accepted...")
    else:
        print("Invalid Username and Password......!")

args('Prathamesh','Khodke')