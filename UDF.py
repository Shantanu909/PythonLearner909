#user defined functions



def greetings():
    print("Hello user")
    
i =0
while(i<5):
    i= i+1    
    greetings()
    
      
def addi(a,b):
    
    sum_temp = a+b
    return sum_temp

print("Welcome to the function for addition of unmbers")
print("Please enter your two nunmbers")
s = int(input("Please enter the first number\n"))
t = int(input("Please enter the other number\n"))
e = addi(s,t)
print(e)
"""
def greet():
    print("Welcome to the method overloading code")
    
def greet(a,b):
    print("Your name is",a+b)

def greet(a):
    print("Your age is: ",int(a))
    
s = input("Please enter your name:")
k = input("Please enter your last name")
l = int (input("Please enter your age"))
greet(s,k)
greet(l)

greet()
"""