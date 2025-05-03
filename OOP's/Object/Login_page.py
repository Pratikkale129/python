for _ in range(3):
    Email=input("Enter your Email ID    :: ")
    password=input("Enter your Password :: ")
    pass1=open("D:\Pratik\File Handling\Password.txt","r")
    File3=pass1.read()
    print("Input File data :: ",File3)
    pass1.close()
        
    if Email=="Pratik@gmail.com" and password==File3:
        print("Login Successfully...")
    else:
        print("Please Relogin")

    new1=open("D:\Pratik\File Handling\password.txt","w")
    Filptr=new1.write(input("Enter your new Password ::"))
    print("Input File data :: ",File3)
    new1.close()

else:
     print("Your Are out of Attempt...!")