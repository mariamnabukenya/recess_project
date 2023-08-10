import os
# file handling
#file =open("name.txt","w")
#file.write("this is the file created using the open function in python")
#file.close

# read from a file 
#file=open("name.txt","r")
#print(file.read)

#delete a file 
#import os
#create=open("data.txt","w")
#os.remove("data.txt")

# exeption handling
# try block tests code for errors
#else keyword defines code to be executed incase no error is encounted
# finally block is executed regardless of errors encounted

try:
    first_number= int(input("Enter first number"))
    second_number=int(input("Enter second number"))
    ans = first_number/second_number
except ValueError:
    print("Only intergers must be input")    
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("There was no error encounted")
finally:
    print("End of programe")    
