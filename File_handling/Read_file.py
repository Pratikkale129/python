# # Open the sample.txt file in D drive in read mode
# # creates a new file if no such file is exists
# file_handle = open("D:\Pratik\File Handling\sample.txt","r")
# file_r = file_handle.read(19)
# print("File_Reading :: ",file_r)
# file_handle.close()


# file_handle = open("D:\Pratik\File Handling\sample.txt","r")
# line1 = file_handle.readline()
# line2 = file_handle.readline()
# print("Line1 Reading :: ",line1)
# print("Line2 Reading :: ",line2)
# file_handle.close()

# Open the sample.txt file in D drive in read mode
# creates a new file if no such file is exists
# file_handle = open("D:\Pratik\File Handling\sample.txt","r")
# filecontent = file_handle.read()
# count = 0
# for i in filecontent:
#     if i.isdigit():
        # count = count+1
# print("Total Digits :: ",count)
# file_handle.close()


file_handle = open("D:\Pratik\File Handling\sample.txt","r")
filecontent = file_handle.read()
alphanumeric = 0
special = 0
for i in filecontent:
    if i.isalnum():
        alphanumeric = alphanumeric+1
    else:
        special = special+1
print("Total Special Symbols :: ",special)
print("Total Alphanumerics   :: ",alphanumeric)
file_handle.close()