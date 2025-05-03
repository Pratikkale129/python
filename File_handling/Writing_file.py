# Open the sample.txt file in D drive in Write mode
# creates a new file if no such file is exists
# file_handle = open("D:\Pratik\File Handling\sample.txt","w")
# file_handle.write("Pray , Trust , Wait")
# file_handle.close()


# Open the sample.txt file in D drive in append mode
# creates if no such file is exists
file_handle = open("D:\Pratik\File Handling\sample.txt","a")
file_handle.write("\nWork in silence , Let your success make noise#####@@@@...!")
file_handle.close()