import sys
print(sys.version)
print("Please enter the file path for your doc:",end="")
file_path = input()
f = open(file_path)

##TASK1: READ FILES
def run1(file_path):
    ##Reading Files in Python
    f = open(file_path)
    print(f.read(),end="")
    print("")
    
    ##Opening Files in Python
    #file_object = open(file_path, 'mode')
    ##Read Mode
   
    f = open(file_path, "rt")
    f = open(file_path, "rb")  # Binary read
    f = open(file_path, "r+")  # Textual read and write
    f = open(file_path, "rt+") # Same as above
    f = open(file_path, "rb+") # Binary read and write

##TASK2: WRITE FILES    
def run2(file_path,inp):
    
    ##Write Mode
    file_path="d.txt"
    f = open(file_path)
    
    f.write(inp)
    print("")

    # f = open(file_path, "wb")  # Binary write
    # f = open(file_path, "w+")  # Textual write and read
    # f = open(file_path, "wt+") # Same as above
    # f = open(file_path, "wb+") # Binary write and read write


##TASK3: APPEND FILES
def run3(file_path):
        
    ##Append Mode
    f = open(file_path, "a")  # Text append
    f = open(file_path, "at") # Same as above
    f = open(file_path, "ab") # Binary append
    
    
##TASK4: CREATE FILES    
def run4(temp_path):
    ##Create Mode
    f = open(temp_path, "x")  # Text create
    # f = open(file_path, "xt") # Same as above
    # f = open(file_path, "xb") # Binary create
    
def run5(file_path):
    import os
    os.remove(file_path)

    
i=1
while(i!=0):
    f = open(file_path,"rt")
    print("Please enter the choice of your operation")
    print("1: Read file")
    print("2: Write file")
    print("3. Append file")
    print("4. Create file")
    print("5. Delete file")
    print("6. Exit")
    print("Please enter your choice")
    choice = input()
    if(choice=='1'):
        run1(file_path)
    elif(choice=='2'):
        inp = input("Please enter your input")
        run2(file_path,inp)
    elif(choice=='3'):
        run3(file_path)
    elif(choice=='4'):
        temp_path = input("Please enter your input")
        run4(temp_path)
    elif(choice=='5'):
        temp_path = input("Please enter your input")
        run5(temp_path)
    elif(choice=='6'):
        i=0
    f.close()


#Read Pats of the File
f = open(file_path)
print(f.read(5))
#print first line only
f = open(file_path)
print(f.readline())
#Read Lines
f = open(file_path)
for line in f:
    print(line, end="")
f = open(file_path)
print(f.readlines(15))
##Close Files
f.close()

with open(file_path):
    file_contents = f.read()

##Deleting Files in Python
import os
os.remove(file_path)


##POST LAB##
#Task 1:
#Write a python code for create a binary file and read operations.
file_path ="a.txt"
f = open(file_path,"xb")
f = open(file_path,"wb")
text_enter = b"1002"
f.write(text_enter)
f = open(file_path,"rb")
x = f.readline()
print(x)


#Task 2:
#Write a statement in Python to perform the following operations
#1. To open a binary file “LOG.DAT” in read mode

#Write a python code for following functions
#readable()

#writable()
#writelines()
#Database Connectivity
#Step 1: Install mysql-connector:
#pip install mysql-connector-python
#Task 1: Python MySQL Database Connection using MySQL Connector
import mysql.connector
from mysql.connector import Error
#create database Electronics
try:
    connection = mysql.connector.connect(host='localhost',database='Electronics', user='pynative',password='pynative@#29')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
